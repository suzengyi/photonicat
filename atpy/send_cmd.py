import sys
import serial

_DEFALT_PORT = "/dev/ttyUSB3"
_DEFALT_BAUDRATE = 115200
_DEFALT_TIMEOUT = 1
_DEFALT_ENCODE='ascii'
_DEBUG = 0
_END_WORDS = ["OK", "ERROR", "ERROR:"]
_log = print if _DEBUG else callable


def _eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def send_cmd(
    cmd, port=_DEFALT_PORT, baudrate=_DEFALT_BAUDRATE, timeout=_DEFALT_TIMEOUT
):
    ret = ""
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        _log(ser.name)
        cmd = bytes(cmd, _DEFALT_ENCODE)
        if cmd[-1] != b"\r":
            cmd += b"\r"
        _log(cmd)
        ser.write(cmd)
        flag = 0
        while flag < 2:
            tmp = ser.readline()
            _log(tmp)
            tmp = tmp.decode(_DEFALT_ENCODE)
            ret += tmp
            if len([x for x in tmp.split(" ") if x.strip() in _END_WORDS]) != 0:
                break
            if len(tmp) == 0 or tmp == "\n":
                flag += 1
        ser.close()
    except serial.serialutil.SerialException as ser_except:
        _eprint(ser_except)
    return ret


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(send_cmd("+".join(sys.argv[1:])))
    else:
        print(f"{sys.argv[0]} usage:")
