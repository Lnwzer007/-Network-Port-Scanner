import socks
import socket
import sys
from datetime import datetime

TARGET_IP = "TYPE HERE" # IP เป้าหมาย
TIMEOUT = 2.5
PORTS = [21, 22, 23, 80, 81, 82, 83, 88, 443, 554, 1935, 5000, 8000, 8080, 9000, 37777]

# ตั้งค่า proxy
PROXY_HOST = "IP PROXY HERE"
PROXY_PORT = # PORT HERE
PROXY_TYPE = socks.SOCKS5 # รองรับ SOCKS5, SOCKS4, HTTP

def init_proxy():
    socks.set_default_proxy(PROXY_TYPE, PROXY_HOST, PROXY_PORT)
    socket.socket = socks.socksocket

def main():
    print("-" * 50)
    print(f"Scanning Mode : [ PROXY ] via {PROXY_HOST}:{PROXY_PORT}")
    print(f"Target IP     : {TARGET_IP}")
    print(f"Started Time  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    init_proxy()

    try:
        for port in PORTS:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(TIMEOUT)
            
            result = s.connect_ex((TARGET_IP, port))
            status = "OPEN" if result == 0 else "CLOSED/TIMEOUT"
            print(f"Port {port:<5} : [ {status} ]")
            
            s.close()

    except KeyboardInterrupt:
        print("\nERROR by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Runtime error: {e}")
        print("ตรวจสอบว่าพร็อกซีเซิร์ฟเวอร์ทำงานอยู่")
        sys.exit(1)

    print("-" * 50)
    print("การสแกนเสร็จสมบูรณ์")

if __name__ == "__main__":
    main()
