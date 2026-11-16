"""Read-only, stdlib-only discovery and bounded retrieval for the design knowledge base."""
from pathlib import Path
import argparse
import json
import os
import sys

SKILL = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def validate_root(path):
    root = Path(path).expanduser().resolve()
    if not (root / 'CATALOG.json').is_file() or not (root / 'AGENTS.md').is_file():
        raise ValueError(f'Not a design knowledge base (requires CATALOG.json and AGENTS.md): {root}')
    catalog = read_json(root / 'CATALOG.json')
    if not isinstance(catalog.get('resources'), list) or not isinstance(catalog.get('projects'), list):
        raise ValueError(f'Invalid catalog structure: {root / "CATALOG.json"}')
    return root, catalog


def discover(explicit, cwd=None, skill=SKILL):
    if explicit:
        return (*validate_root(explicit), '--kb-root')
    override = os.environ.get('DESIGN_KNOWLEDGE_BASE')
    if override:
        return (*validate_root(override), 'DESIGN_KNOWLEDGE_BASE')
    config = skill / 'config.local.json'
    if config.is_file():
        settings = read_json(config)
        if not isinstance(settings.get('kb_root'), str) or not settings['kb_root'].strip():
            raise ValueError(f'Expected a non-empty kb_root in {config}')
        configured = Path(settings['kb_root']).expanduser()
        if not configured.is_absolute():
            configured = config.parent / configured
        return (*validate_root(configured), 'config.local.json')
    here = Path(cwd or Path.cwd()).resolve()
    seen = set()
    candidates = [*skill.parents]
    for parent in [here, *here.parents]:
        candidates.extend([parent, parent / 'design-knowledge-base'])
    for candidate in candidates:
        candidate = candidate.resolve()
        if candidate in seen:
            continue
        seen.add(candidate)
        if (candidate / 'CATALOG.json').is_file() and (candidate / 'AGENTS.md').is_file():
            return (*validate_root(candidate), 'repository-or-working-directory')
    raise ValueError('Knowledge base not found. Pass --kb-root or set DESIGN_KNOWLEDGE_BASE, or configure this skill\'s config.local.json.')


def contained_file(root, relative):
    if not isinstance(relative, str) or Path(relative).is_absolute() or '\\' in relative or '..' in Path(relative).parts:
        raise ValueError(f'Expected a catalog-relative file path: {relative}')
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f'Catalog path escapes the knowledge base: {relative}')
    if not path.is_file():
        raise ValueError(f'Catalog file missing: {relative}')
    return str(path)


def resource_paths(root, catalog, resource):
    result = dict(resource)
    for key in ['doc_path', 'spec_path']:
        result[key] = contained_file(root, resource[key]) if resource.get(key) else None
    for key in ['documents', 'example_paths']:
        result[key] = [contained_file(root, p) for p in resource.get(key, [])]
    project = next((p for p in catalog['projects'] if p['id'] == resource['project']), None)
    if project:
        manifest_path = contained_file(root, project['manifest_path'])
        folder = Path(project['manifest_path']).parent
        result['project_context'] = {
            'manifest': manifest_path,
            'design_overview': contained_file(root, (folder / 'design-language/overview.md').as_posix()),
            'license_notes': contained_file(root, (folder / 'LICENSE-NOTES.md').as_posix()),
        }
    return result


def search(root, catalog, args):
    terms = args.query.casefold().split()
    found = []
    for r in catalog['resources']:
        if args.project and args.project != r['project']:
            continue
        if args.type and args.type != r['resource_type']:
            continue
        if args.platform and args.platform.casefold() not in [p.casefold() for p in r['platforms']]:
            continue
        hay = ' '.join([r['id'], r['name'], r['description'], *r.get('keywords', []), *r.get('original_stack', [])]).casefold()
        if all(term in hay for term in terms):
            found.append(r)
    found.sort(key=lambda r: (r['id'].casefold() != args.query.casefold(), r['id']))
    rows = []
    for r in found[:args.limit]:
        resolved = resource_paths(root, catalog, r)
        rows.append({k: resolved[k] for k in ['id', 'project', 'name', 'description', 'doc_path', 'spec_path', 'verification', 'license']})
    return {'matches': len(found), 'returned': len(rows), 'resources': rows}


def tokens(root, catalog, args):
    project = next((p for p in catalog['projects'] if p['id'] == args.project), None)
    if not project:
        raise ValueError(f'Unknown project: {args.project}')
    folder = Path(project['manifest_path']).parent
    path = contained_file(root, (folder / 'design-language/tokens.json').as_posix())
    payload = read_json(Path(path))
    found = []
    for token in payload['tokens']:
        if args.name.casefold() not in token['name'].casefold():
            continue
        inherited = token.get('definition_scope', '').startswith(':root')
        if args.theme and token['theme'] not in [args.theme, 'all'] and not (inherited and args.theme in token.get('effective_theme_expressions', {})):
            continue
        result = dict(token)
        if args.theme:
            result['requested_theme'] = args.theme
            result['effective_expression'] = token.get('effective_theme_expressions', {}).get(args.theme, token['value'])
        found.append(result)
    return {'project': args.project, 'commit': payload['commit'], 'tokens_file': path,
            'matches': len(found), 'returned': min(len(found), args.limit), 'tokens': found[:args.limit]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--kb-root', help='Explicit knowledge-base directory; takes precedence over local discovery')
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('locate', help='Return knowledge-base entry paths without loading project contents')
    query = commands.add_parser('search', help='Search catalog metadata with a few keywords')
    query.add_argument('query', nargs='?', default='')
    query.add_argument('--project', default='')
    query.add_argument('--platform', default='')
    query.add_argument('--type', default='')
    query.add_argument('--limit', type=int, choices=range(1, 51), default=6, metavar='1..50')
    resolve = commands.add_parser('resolve', help='Resolve one stable ID to exact local document/spec/example paths')
    resolve.add_argument('id')
    token_query = commands.add_parser('tokens', help='Return only relevant tokens, preserving provenance and theme expressions')
    token_query.add_argument('--project', required=True)
    token_query.add_argument('--name', default='')
    token_query.add_argument('--theme', default='')
    token_query.add_argument('--limit', type=int, choices=range(1, 51), default=6, metavar='1..50')
    args = parser.parse_args(argv)
    try:
        root, catalog, method = discover(args.kb_root)
        if args.command == 'locate':
            result = {'kb_root': str(root), 'discovered_by': method,
                      'catalog': str(root / 'CATALOG.json'), 'agents': str(root / 'AGENTS.md'),
                      'projects': [p['id'] for p in catalog['projects']], 'resources': len(catalog['resources'])}
        elif args.command == 'search':
            result = search(root, catalog, args)
        elif args.command == 'resolve':
            resource = next((r for r in catalog['resources'] if r['id'] == args.id), None)
            if resource is None:
                raise ValueError(f'Unknown resource ID: {args.id}. Search the current catalog first.')
            result = resource_paths(root, catalog, resource)
        else:
            result = tokens(root, catalog, args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, KeyError) as error:
        print(json.dumps({'error': str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    raise SystemExit(main())
