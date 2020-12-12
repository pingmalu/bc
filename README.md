# bc
Beyond Compare 命令行辅助工具

使用方法：

```
python bc.py [git log file path] [env]
```

```
python bc.py [Beyond Compare session name]
```

配置说明:

```json
{
    "BCompare_path": "这里填BCompare.exe文件路径",
    "主目录路径": {
        "default": "比对路径",
        "test": "比对路径",
        "prod": "比对路径",
        "open_session": {
            "default": "会话名称",
            "web": "会话名称",
            "test": "会话名称",
            "prod": "会话名称"
        }
    }
}
```

配置 demo:

```json
{
    "BCompare_path": "C:\\\\02_SOFT\\\\Xshell\\\\Beyond Compare 4\\\\BCompare.exe",
    "C:\\01_cloud\\gitlab\\16988": {
        "default": "profile:root@192.168.1.200?/Projects/PHP/bric",
        "test": "C:\\01_cloud\\gitlab\\16988_test",
        "prod": "C:\\01_cloud\\gitlab\\16988_prod",
        "open_session": {
            "default": "16988-online",
            "web": "16988-online-web",
            "test": "16988-test",
            "prod": "16988-prod"
        }
    }
}
```

编译成可执行文件：

```shel
pyinstaller --distpath .\out -F bc.py -w -n bc.exe
```

开发环境运行：

```
C:/Users/ml/.conda/envs/py36/python.exe C:/01_cloud/gitlab/bc/bc.py test
```

