"""Behavior checks for read-only discovery, retrieval and portable skill installation."""
from pathlib import Path
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/design-knowledge-base'
spec = importlib.util.spec_from_file_location('design_kb_skill', SKILL / 'scripts/kb.py')
kb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb)


class SkillBehavior(unittest.TestCase):
    def setUp(self):
        self.catalog = kb.read_json(ROOT / 'CATALOG.json')

    def test_platform_and_project_filters_and_output_limit(self):
        args = SimpleNamespace(query='focus', project='droiddeck', platform='Android', type='animation', limit=1)
        result = kb.search(ROOT, self.catalog, args)
        self.assertEqual(result['returned'], 1)
        self.assertTrue(all(r['project'] == 'droiddeck' for r in result['resources']))
        args.platform = 'Windows'
        self.assertEqual(kb.search(ROOT, self.catalog, args)['matches'], 0)

    def test_resource_paths_retain_license_and_verification(self):
        resource = next(r for r in self.catalog['resources'] if r['id'] == 'droiddeck.animation.focus-glide')
        result = kb.resource_paths(ROOT, self.catalog, resource)
        self.assertEqual(result['license'], 'GPL-3.0')
        self.assertNotIn('runtime-verified', result['verification'])
        self.assertTrue(Path(result['spec_path']).is_file())
        self.assertTrue(Path(result['project_context']['license_notes']).is_file())

    def test_dark_mode_inherited_css_role_is_discoverable(self):
        args = SimpleNamespace(project='cherry-studio', name='--background', theme='dark', limit=50)
        result = kb.tokens(ROOT, self.catalog, args)
        inherited = next(t for t in result['tokens'] if t['name'] == '--background')
        self.assertTrue(inherited['definition_scope'].startswith(':root'))
        self.assertEqual(inherited['requested_theme'], 'dark')
        self.assertNotEqual(inherited['effective_expression'], 'var(--cs-background)')
        self.assertNotEqual(inherited['effective_expression'], inherited['effective_theme_expressions']['light'])
        self.assertIn('source', inherited)

    def test_explicit_root_wins_over_invalid_environment(self):
        with patch.dict(os.environ, {'DESIGN_KNOWLEDGE_BASE': str(ROOT / 'missing')}):
            root, _, method = kb.discover(str(ROOT))
        self.assertEqual(root, ROOT)
        self.assertEqual(method, '--kb-root')

    def test_invalid_explicit_root_does_not_silently_fallback(self):
        with self.assertRaises(ValueError):
            kb.discover(str(ROOT / 'missing'))

    def test_invalid_config_does_not_fallback_to_current_repository(self):
        with tempfile.TemporaryDirectory() as folder, patch.dict(os.environ, {}, clear=True):
            fake_skill = Path(folder)
            (fake_skill / 'config.local.json').write_text('{"kb_root":"missing"}', encoding='utf-8')
            with self.assertRaises(ValueError):
                kb.discover(None, cwd=ROOT, skill=fake_skill)

    def test_catalog_cannot_escape_root(self):
        with tempfile.TemporaryDirectory() as folder:
            parent = Path(folder)
            root = parent / 'kb'
            root.mkdir()
            outside = parent / 'outside.txt'
            outside.write_text('outside fixture', encoding='utf-8')
            with self.assertRaises(ValueError):
                kb.contained_file(root, '../outside.txt')
            self.assertEqual(outside.read_text(encoding='utf-8'), 'outside fixture')

    def test_installed_copy_locates_kb_from_unrelated_working_directory(self):
        with tempfile.TemporaryDirectory(prefix='skill path with spaces-') as folder:
            installed = Path(folder) / 'installed-skill'
            shutil.copytree(SKILL, installed, ignore=shutil.ignore_patterns('__pycache__', 'config.local.json'))
            (installed / 'config.local.json').write_text(json.dumps({'kb_root': str(ROOT)}), encoding='utf-8')
            env = dict(os.environ)
            env.pop('DESIGN_KNOWLEDGE_BASE', None)
            result = subprocess.run([sys.executable, '-X', 'utf8', str(installed / 'scripts/kb.py'), 'locate'], cwd=folder, env=env, capture_output=True, text=True, encoding='utf-8')
            self.assertEqual(result.returncode, 0, result.stderr)
            located = json.loads(result.stdout)
            self.assertEqual(Path(located['kb_root']), ROOT)
            self.assertEqual(located['discovered_by'], 'config.local.json')

    def test_unknown_id_cli_reports_error_without_traceback(self):
        result = subprocess.run([sys.executable, '-X', 'utf8', str(SKILL / 'scripts/kb.py'), '--kb-root', str(ROOT), 'resolve', 'missing.resource'], capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, 2)
        self.assertIn('Unknown resource ID', json.loads(result.stderr)['error'])


if __name__ == '__main__':
    result = unittest.TextTestRunner(stream=sys.stderr, verbosity=1).run(unittest.defaultTestLoader.loadTestsFromTestCase(SkillBehavior))
    print(json.dumps({'result': 'passed' if result.wasSuccessful() else 'failed', 'tests_run': result.testsRun,
                      'scope': 'read-only discovery, project/platform filters, bounded output, provenance, inherited dark tokens, explicit path precedence, portable local config and path boundary'}))
    raise SystemExit(0 if result.wasSuccessful() else 1)
