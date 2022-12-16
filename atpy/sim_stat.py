# AT+QSIMSTAT?
# +QSIMSTAT: 0,1
from send_cmd import send_cmd

def print_return(ret_str):
    enable,inserted_status=ret_str.split(":")[-1].split(",")
    print("上报状态变化：\t",end="")
    print("开") if int(enable) else print("关")
    print("SIM卡插入状态：\t",end="")
    print("开") if int(inserted_status) else print("关")

if __name__=="__main__":
    print_return(send_cmd("AT+QSIMSTAT?").splitlines()[1])