# AT+CMGD=1,3
from send_cmd import send_cmd
import sys

def print_return(ret_str):
    if ret_str.startswith("OK"):
        print("删除成功")
    else:
        print("删除失败")

if __name__=="__main__":
    if len(sys.argv)>1 and sys.argv[1]=="YES":
        print_return(send_cmd(f"AT+CMGD=1,3").splitlines()[-1])
    else:
        print("参数填入YES以删除所有短信")
    