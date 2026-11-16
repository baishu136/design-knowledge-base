# 持续更新流程

1. 新版本下载到新的Commit命名快照；保留旧快照和本库资料。记录获取方式、分支、Commit日期、归档哈希。
2. 对比旧/新Git树或file-inventory SHA256，先筛选UI、主题、motion、依赖锁文件的变化。不得在原快照安装/格式化/构建。
3. 利用source-map找到受影响资源；变更设计意图与实现参数分别复核。更新依赖默认值时记录依赖版本与来源，仍未知则null。
4. 更新tools/author.py中的来源与分析；资源ID沿用，废弃项添加superseded_by而非复用旧ID代表不同效果。
5. 当前scan缓存以manifest.commit命中；切换Commit必须用全新manifest或删除**知识库生成缓存**后重扫，不能只手改manifest骗过缓存。原始文件不删。
6. 重建项目资料，运行check-examples与validate。原生平台示例要在独立宿主工程验证，禁止把源码静态验证提升为runtime。
7. 更新示例example.json、CHANGELOG、EXECUTION-REPORT和BACKLOG；重新生成CATALOG。检查所有关联ID、路径和出处。

## 当前结构

author.py为本轮人工分析内容的可重放作者数据；build.py为通用写入与候选扫描；publish.py为索引/文档模板；validate.py为结构、路径、参数证据与来源完整性检查。每次修改生成文件，先核对对应作者入口。未来可将author数据拆为每项目文件，但不得把不同项目的规则合并。

## 快照获取说明

Cherry两仓及DroidDeck使用GitHub codeload按Commit获取归档并记录SHA256；Mihon使用depth1 Git clone。DroidDeck归档未递归包含MaliBridge/Syncthing子模块，覆盖仅指超级项目已有文件。仓库之外的源码不是知识库发布物的一部分；归档/复制时同时保存所需来源和许可证。早期中断的cherry-studio与cherry-studio-app克隆目录、以及desktop review-files只用于获取过程，均不是manifest指向的分析快照；不纳入覆盖率。
