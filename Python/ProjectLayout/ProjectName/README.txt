1. setup.py : Python安装脚本的标准名称。
2. README.txt : 为用户提供相关说明。
3. requirements.txt : 包含Python包所需要的依赖包。
4. test-requirements.txt : 列出运行测试集所需要的依赖包。
5. docs : 应该包含reStructuredText格式的文档，以便能被Sphinx处理。
6. etc : 存放配置文件样例。
7. tools : 存放于工具有关的shell脚本。
8. bin : 存放将被python.py安装的二进制脚本
9. data : 存放其它类型的文件，如媒体文件等。

避免创建只有一个__init__.py文件的目录。如果创建目录，那么其中就应该包含属于模块的多个Python文件。