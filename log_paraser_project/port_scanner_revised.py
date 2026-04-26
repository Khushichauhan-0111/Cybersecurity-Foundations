import socket
import threading
from queue import Queue
from datetime import datetime
PORT_INFO = {
    21:   ("FTP", "Critical - Unencrypted"),
    22:   ("SSH", "Secure - Brute Force Risk"),
    23:   ("Telnet", "Critical - Unencrypted"),
    25:   ("SMTP", "Medium - Mail Server"),
    53:   ("DNS", "Standard"),
    80:   ("HTTP", "Medium - Unencrypted"),
    443:  ("HTTPS", "Secure"),
    445:  ("SMB", "Critical - Ransomware Target"),
    3306: ("MySQL", "High - Database"),
    3389: ("RDP", "Critical - Remote Desktop")
}
RED = '\033[91m'
RESET = '\033[0m'

queue = Queue()
open_ports = []
print_lock = threading.Lock()

def get_banner(s):
    try:
        s.send(b'Hello\r\n')
        banner = s.recv(1024).decode(errors='ignore').strip()
        return "".join(char for char in banner if char.isprintable())[:50]
    except:
        return "No response"

def port_scan(target):
    while not queue.empty():
        port = queue.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.5)
            if s.connect_ex((target, port)) == 0:
                banner = get_banner(s)
                service, threat = PORT_INFO.get(port, ("Unknown", "Unknown Risk"))
                if "Critical" in threat or "High" in threat:
                    threat_display = f"{RED}{threat}{RESET}"
                else:
                    threat_display = threat

                with print_lock:
                    open_ports.append((port, service, banner, threat_display))
            s.close()
        except:
            pass
        finally:
            queue.task_done()

def run_scanner():
    print("-" * 80)
    print("PORT SCANNER - SERVICE ENUMERATION")
    print("-" * 80)

    target = input("Target Host: ")
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\nError: Could not resolve hostname.")
        return

    start_p = int(input("Start Port: "))
    end_p = int(input("End Port: "))

    print(f"\nScanning {target} ({target_ip})...\n")

    for port in range(start_p, end_p + 1):
        queue.put(port)

    for _ in range(100):
        t = threading.Thread(target=port_scan, args=(target_ip,))
        t.daemon = True
        t.start()

    queue.join()

    print(f"{'PORT':<7} {'SERVICE':<12} {'BANNER/VERSION':<30} {'THREAT ASSESSMENT'}")
    print("-" * 80)

    if not open_ports:
        print("No open ports detected.")
    else:
        for p, s, b, t in sorted(open_ports):
            print(f"{p:<7} {s:<12} {b:<30} {t}")

    print("-" * 80)
    print(f"Scan Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

if __name__ == "__main__":
    try:
        run_scanner()
    except KeyboardInterrupt:
        print("\nUser Aborted.")
