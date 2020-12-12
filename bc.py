# Beyond Compare 命令行辅助工具
# author : Malu
# Since : 2020-12-12
# Usage : python bc.py [git log file path] [env]
#         python bc.py [Beyond Compare session name]
# Config demo:
# {
#     "BCompare_path": "C:\\\\02_SOFT\\\\Xshell\\\\Beyond Compare 4\\\\BCompare.exe",
#     "C:\\01_cloud\\gitlab\\16988": {
#         "default": "profile:root@192.168.1.200?/Projects/PHP/bric",
#         "test": "C:\\01_cloud\\gitlab\\16988_test",
#         "prod": "C:\\01_cloud\\gitlab\\16988_prod",
#         "open_session": {
#             "default": "16988-online",
#             "web": "16988-online-web",
#             "test": "16988-test",
#             "prod": "16988-prod"
#         }
#     }
# }
import sys
import os
import json


def main():
    conf_name = "conf.json"
    
    # 当前执行文件的路径
    json_path = os.path.split(os.path.realpath(__file__))[0]+"/"+conf_name
    
    # 拿到pyinstaller编译后的exe文件路径
    json_path_default = os.path.split(sys.executable)[0]+"/"+conf_name
    
    # print(json_path)
    # print(json_path_default)

    # 先从exe所在的默认路径获取配置，如果失败则从执行目录获取配置
    try:
        with open(json_path_default, 'r') as f:
            dict = json.load(f)
    except:
        try:
            with open(json_path, 'r') as f:
                dict = json.load(f)
        except:
            print("can not load json file: "+json_path)
            return

    # 读取BCompare文件路径
    try:
        BCompare_path = dict["BCompare_path"]
    except:
        print("BCompare_path not found")
        return

    # 获取第一参数，默认""
    try:
        filename = sys.argv[1]
    except:
        filename = ""

    # 获取第二参数，默认"default"
    try:
        flag = sys.argv[2]
    except IndexError:
        flag = "default"

    # 获取比较路径
    pwd = os.getcwd()
    try:
        remotepath = dict[pwd][flag]
    except:
        print("No such directory in config dict")
        return

    # 通过第一个参数寻找open_session中配置的会话
    try:
        if filename == "":
            open_session = dict[pwd]["open_session"]["default"]
        else:
            open_session = dict[pwd]["open_session"][filename]
    except:
        open_session = False

    # 本地文件地址
    myfile = pwd+"/"+filename
    # 待比较文件地址
    remotefile = remotepath+"/"+filename

    # 执行脚本
    bcpath = r'start "" "'+BCompare_path+r'"'

    if open_session:
        allpath = bcpath+" \""+open_session+"\""
    else:
        allpath = bcpath+" \""+myfile+"\""+" \""+remotefile+"\""
    # print(allpath)
    os.system(allpath)


if __name__ == '__main__':
    main()
