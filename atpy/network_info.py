# AT+QNWINFO
# +QNWINFO: "NR5G-SA",46001,"NR N78",627264
from send_cmd import send_cmd

carrier_dict={
    46000:"中国移动(GSM)",
    46001:"中国联通(GSM)",
    46002:"中国移动(TD-S)",
    46003:"中国电信(CDMA)",
    46005:"中国电信(CDMA)",
    46006:"中国联通(wCDMA)",
    46007:"中国移动(TD-S)",
    46008:"中国移动",
    46011:"中国电信(FDD-LTE)",
    46015:"中国广电"
}

def print_return(ret_str):
    act,oper,band,channel=ret_str.split(":")[-1].split(",")
    act=act.strip("\" ")
    band=band.strip("\"")
    print(f"网络类型：\t{act}")
    print(f"运营商：\t{oper}" + (f"（{carrier_dict[int(oper)]}）" 
        if int(oper) in carrier_dict else ""))
    print(f"频  段：\t{band}")
    print(f"信道ID：\t{channel}")

if __name__=="__main__":
    print_return(send_cmd("AT+QNWINFO").splitlines()[1])