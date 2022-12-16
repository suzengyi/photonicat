# AT+QSIMSTAT?
# +QSIMSTAT: 0,1
from send_cmd import send_cmd
import sys

def parse_param(param):
    dic={3:"WCDMA",4:"LTE",5:"NR5G"}
    ret=[]
    if param is list:
        param="".join(param)
    for ch in param:
        if not ch.isdecimal():
            continue
        if int(ch) in dic:
            ret.append(dic.pop(int(ch)))
    return ":".join(ret)

def print_return(ret_str):
    if ret_str.startswith("OK"):
        print("配置成功")
    else:
        print("配置失败")

if __name__=="__main__":
    if len(sys.argv)>1:
        param=parse_param(sys.argv[1:])
    else:
        param="AUTO"
    print(f"将网络搜索模式设置为：{param}")
    print_return(send_cmd(f"AT+QNWPREFCFG=\"mode_pref\",{param}").splitlines()[-1])