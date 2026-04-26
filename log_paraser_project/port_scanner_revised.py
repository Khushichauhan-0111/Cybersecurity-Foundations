# import socket
# import threading
# from queue import Queue

# # 1. Database of common ports and their safety status
# PORT_INFO = {
#     21:  ("FTP", "⚠️ High (Unencrypted file transfer)"),
#     22:  ("SSH", "✅ Secure (Encrypted remote access)"),
#     23:  ("Telnet", "❌ Critical (Unencrypted - Big security risk)"),
#     25:  ("SMTP", "⚠️ Medium (Email - Often targeted for spam)"),
#     53:  ("DNS", "✅ Standard"),
#     80:  ("HTTP", "⚠️ Medium (Unencrypted web traffic)"),
#     443: ("HTTPS", "✅ Secure (Encrypted web traffic)"),
#     3306:("MySQL", "⚠️ High (Database - Should not be public)"),
#     3389:("RDP", "❌ Critical (Remote Desktop - Frequent attack target)")
# }

# # Thread-safe queue to hold ports
# queue = Queue()
# open_ports = []

# def port_scan(target, port):
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.settimeout(0.5) # Fast timeout for multithreading
#         if s.connect_ex((target, port)) == 0:
#             # Get info from our database
#             service, threat = PORT_INFO.get(port, ("Unknown Service", "ℹ️ Unknown Risk"))
#             open_ports.append((port, service, threat))
#         s.close()
#     except:
#         pass

# def worker(target):
#     while not queue.empty():
#         port = queue.get()
#         port_scan(target, port)
#         queue.task_done()

# def run_scanner():
#     target = input("Enter Target IP/Host (e.g. 127.0.0.1): ")
#     start_p = int(input("Enter Start Port: "))
#     end_p = int(input("Enter End Port: "))

#     # Fill the queue with ports
#     for port in range(start_p, end_p + 1):
#         queue.put(port)

#     # Start 100 threads for speed
#     print(f"\nScanning {target}... please wait.\n")
#     for _ in range(100):
#         t = threading.Thread(target=worker, args=(target,))
#         t.daemon = True
#         t.start()

#     queue.join() # Wait for all threads to finish

#     # Display Results
#     print("-" * 60)
#     print(f"{'PORT':<10} {'SERVICE':<20} {'THREAT LEVEL'}")
#     print("-" * 60)
#     for p, s, t in sorted(open_ports):
#         print(f"{p:<10} {s:<20} {t}")

# if __name__ == "__main__":
#     run_scanner()

# import socket
# import threading
# from queue import Queue
# from datetime import datetime

# # --- DATABASE ---
# # Mapping common ports to their typical services and security risk levels
# PORT_INFO = {
#     21:   ("FTP", "❌ Critical (Passwords sent in plain text)"),
#     22:   ("SSH", "✅ Secure (But prone to brute-force password guesses)"),
#     23:   ("Telnet", "❌ Critical (Highly insecure, unencrypted)"),
#     25:   ("SMTP", "⚠️ Medium (Mail server - check for open relays)"),
#     53:   ("DNS", "✅ Standard"),
#     80:   ("HTTP", "⚠️ Medium (Unencrypted web traffic)"),
#     110:  ("POP3", "⚠️ Medium (Email - use IMAPS/POP3S instead)"),
#     135:  ("RPC", "⚠️ Medium (Windows Remote Procedure Call)"),
#     139:  ("NetBIOS", "⚠️ High (Legacy Windows networking)"),
#     443:  ("HTTPS", "✅ Secure (Encrypted web traffic)"),
#     445:  ("SMB", "❌ Critical (Often used by Ransomware like WannaCry)"),
#     3306: ("MySQL", "⚠️ High (Database - should never be public)"),
#     3389: ("RDP", "❌ Critical (Remote Desktop - prime target for hackers)"),
#     8080: ("HTTP-Proxy", "⚠️ Medium (Often used for dev environments)")
# }

# # --- GLOBAL VARIABLES ---
# queue = Queue()
# open_ports = []
# print_lock = threading.Lock() # Prevents text from overlapping in the console

# def get_banner(s):
#     """Attempts to grab a service banner to identify software versions."""
#     try:
#         # Some services (like SSH) send a banner immediately.
#         # Others need a 'nudge' to respond.
#         s.send(b'Hello\r\n')
#         banner = s.recv(1024).decode(errors='ignore').strip()
#         # Filter out non-printable characters for a clean output
#         return "".join(char for char in banner if char.isprintable())[:50]
#     except:
#         return "No banner (Quiet Service)"

# def port_scan(target):
#     """The main logic for checking a single port."""
#     while not queue.empty():
#         port = queue.get()
#         try:
#             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             s.settimeout(1.5) # Time allowed for the 'knock' and 'hello'
            
#             result = s.connect_ex((target, port))
            
#             if result == 0:
#                 banner = get_banner(s)
#                 service, threat = PORT_INFO.get(port, ("Unknown", "ℹ️ Unknown Risk"))
                
#                 # Using a lock ensures the print statements don't jumble up
#                 with print_lock:
#                     open_ports.append((port, service, threat, banner))
            
#             s.close()
#         except Exception:
#             pass
#         finally:
#             queue.task_done()

# def run_scanner():
#     print("-" * 60)
#     print("      🚀 PROFESSIONAL MULTITHREADED PORT SCANNER")
#     print("-" * 60)

#     target = input("Enter Target (e.g., 127.0.0.1 or scanme.nmap.org): ")
#     try:
#         target_ip = socket.gethostbyname(target)
#     except socket.gaierror:
#         print("\n[!] Error: Could not resolve hostname.")
#         return

#     start_p = int(input("Enter Starting Port: "))
#     end_p = int(input("Enter Ending Port: "))

#     print(f"\nScanning {target} ({target_ip})...")
#     print(f"Started at: {datetime.now().strftime('%H:%M:%S')}\n")

#     # Load ports into the queue
#     for port in range(start_p, end_p + 1):
#         queue.put(port)

#     # Start 100 worker threads
#     for _ in range(100):
#         t = threading.Thread(target=port_scan, args=(target_ip,))
#         t.daemon = True
#         t.start()

#     # Wait for all threads to finish
#     queue.join()

#     # --- FINAL REPORT ---
#     print("\n" + "=" * 85)
#     print(f"{'PORT':<7} {'SERVICE':<12} {'BANNER/VERSION':<25} {'THREAT ASSESSMENT'}")
#     print("=" * 85)

#     if not open_ports:
#         print("No open ports found in the specified range.")
#     else:
#         # Sort by port number before printing
#         for p, s, t, b in sorted(open_ports):
#             print(f"{p:<7} {s:<12} {b:<25} {t}")

#     print("=" * 85)
#     print(f"Scan Completed at: {datetime.now().strftime('%H:%M:%S')}\n")

# if __name__ == "__main__":
#     try:
#         run_scanner()
#     except KeyboardInterrupt:
#         print("\n\n[!] Scan stopped by user. Exiting...")

import socket
import threading
from queue import Queue
from datetime import datetime

# --- CONFIGURATION ---
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

# ANSI Escape Codes for Colors
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
                
                # Apply red color if threat level is Critical or High
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