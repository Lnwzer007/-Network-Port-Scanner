import socket
import sys
from datetime import datetime

TARGET_IP = "TYPE HERE" # IP เป้าหมาย
TIMEOUT = 1.5
PORTS = [21, 22, 23, 80, 81, 82, 83, 88, 443, 554, 1935, 5000, 8000, 8080, 9000, 37777]

def main():
    print("-" * 50)
    print(f"Scanning Mode : [ DIRECT ]")
    print(f"Target IP     : {TARGET_IP}")
    print(f"Started Time  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    try:
        for port in PORTS:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(TIMEOUT)
            
            result = s.connect_ex((TARGET_IP, port))
            status = "OPEN" if result == 0 else "CLOSED"
            print(f"Port {port:<5} : [ {status} ]")
            
            s.close()

    except KeyboardInterrupt:
        print("\nExecution interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[Runtime error: {e}")
        sys.exit(1)

    print("-" * 50)
    print("การสแกนเสร็จสมบูรณ์")

if __name__ == "__main__":
    main()
