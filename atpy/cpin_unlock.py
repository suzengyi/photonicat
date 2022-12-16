from send_cmd import send_cmd
import sys

def pin_check(pin_str:str)->bool:
    return len(pin_str)==4 and pin_str.isdecimal()

def pin_unlock(pincode:int):
    cmd = f"AT+CPIN=\"{pincode}\""
    ret = send_cmd(cmd)
    if ret[-4:-2]=="OK":
        return True
    else:
        return False

if __name__=="__main__":
    if len(sys.argv) > 1:
        if not pin_check(sys.argv[1]):
            print(f"{sys.argv[1]} is not a legal pin code")
            exit()
        if pin_unlock(int(sys.argv[1])):
            print("unlock success")
        else:
            print("unlock failed, input pin code is "+sys.argv[1])
    else:
        print(sys.argv[0])