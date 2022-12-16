# python "/root/atpy/send_cmd.py" AT CMGL
'''
pip install smspdudecoder
0 已接收但未读的短消息
1 已接收且已读的短消息
2 已存储但未发送的短消息
3 已存储且已发送的短消息
4 所有短消息

AT+CMGL
+CMGL: 1,1,,24
0891683110102105F0040D91685156701523F0000822213122706323046D4B8BD5
+CMGL: 2,0,,24
0891683110102105F0040D91685156701523F0000822213132222023046D4B8BD5

OK

{'sender': '+8615650751320', 'date': datetime.datetime(2022, 12, 13, 14, 7, 36, tzinfo=datetime.timezone.utc), 'content': '测试', 'partial': False}
'''
from smspdudecoder.easy import easy_sms
from send_cmd import send_cmd
import sys

def print_sms(msg):
    print(f'''发信人：{msg['sender']}
时间：{msg['date'].strftime('UTC %Y-%m-%d %H:%M:%S')}
内容：{msg['content']}
    ''')

def parse_ret(ret):
    stat_dict={
        0:"已接收但未读的短消息",
        1:"已接收且已读的短消息",
        2:"已存储但未发送的短消息",
        3:"已存储且已发送的短消息",
        4:"所有短消息"
    }
    ret = ret.splitlines()
    for i in range(1,len(ret),2):
        if len(ret)<=i+1 or ret[i+1].startswith("OK"):break
        heads=ret[i].split(":")[1].split(",")
        print(f"编号：{heads[0]}")
        print(f"状态：{stat_dict[int(heads[1])]}")
        print_sms(easy_sms(ret[i+1]))

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1].isdecimal():
        stat=int(sys.argv[1])
    else :stat=0
    parse_ret(send_cmd("AT+CMGL"))