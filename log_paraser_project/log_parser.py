# import os

# def parse_logs(log_file):
#     # Dictionary to store IP: count
#     failed_attempts = {}

#     with open(log_file, 'r') as f:
#         for line in f:
#             if "ERROR" in line and "Failed login" in line:
#                 # Extract the IP address
#                 # Assuming format: ...from 192.168.1.50
#                 try:
#                     ip = line.split("from")[-1].strip()
#                     if ip:
#                         failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
#                 except:
#                     continue
#     return failed_attempts

# if __name__ == "__main__":
#     # Get the directory of this script to handle paths correctly
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     log_file_path = os.path.join(script_dir, "server_traffic.log")

#     # Analyze
#     failed_ips = parse_logs(log_file_path)

#     # Threshold Detection
#     threshold = 2
#     print("--- Security Alert: Potential Brute Force Detected ---")
#     for ip, count in failed_ips.items():
#         if count > threshold:
#             print(f"ALERT: IP {ip} exceeded threshold with {count} failed attempts!")
#         else:
#             print(f"Status: IP {ip} has {count} failed attempts.")



# import os

# # ANSI Color Codes
# RED = '\033[91m'
# RESET = '\033[0m'

# def analyze_port_risk(port):
#     """Provides a specific action plan based on the targeted port."""
#     print(f"{RED}[!] SECURITY PROTOCOL FOR PORT {port}:{RESET}")
#     if port == "22":
#         print("    STATUS: SSH Attack Detected.")
#         print("    ACTION: Change admin passwords and enable SSH-Key only login.")
#     elif port == "445":
#         print("    STATUS: SMB/Ransomware Pattern Detected.")
#         print("    ACTION: CRITICAL! Isolate system and verify offline backups.")
#     else:
#         print("    STATUS: Unknown service targeted.")
#         print("    ACTION: Monitor traffic and block source IP at firewall.")

# def parse_logs(log_file):
#     failed_ips = {}
#     failed_users = {}
#     threshold = 2

#     if not os.path.exists(log_file):
#         print(f"Error: {log_file} not found.")
#         return

#     with open(log_file, 'r') as f:
#         print("-" * 60)
#         print("SEARCHING LOGS FOR THREATS...")
#         print("-" * 60)

#         for line in f:
#             # 1. Detect Port Attacks
#             if "Unauthorized access attempt on port" in line:
#                 port = line.split("port")[-1].strip()
#                 analyze_port_risk(port)
#                 print("-" * 60)

#             # 2. Detect Failed Logins (Tracking IPs and Usernames)
#             if "Failed login" in line:
#                 try:
#                     # Extract IP (the part after 'from')
#                     ip = line.split("from")[-1].strip()
#                     # Extract User (the part between the single quotes)
#                     user = line.split("user")[-1].split("'")[1]

#                     failed_ips[ip] = failed_ips.get(ip, 0) + 1
#                     failed_users[user] = failed_users.get(user, 0) + 1
#                 except IndexError:
#                     continue

#     # --- FINAL SUMMARY REPORT ---
#     print("\n" + "=" * 60)
#     print("INCIDENT SUMMARY REPORT")
#     print("=" * 60)

#     # Report by IP
#     for ip, count in failed_ips.items():
#         if count > threshold:
#             print(f"{RED}BRUTE FORCE:{RESET} IP {ip} failed {count} times.")

#     # Report by User (To catch attackers changing IPs)
#     for user, count in failed_users.items():
#         if count > threshold:
#             print(f"{RED}TARGETED USER:{RESET} Account '{user}' attacked {count} times.")
#             print(f"    RECO: Lock account '{user}' and notify actual owner.")

#     print("=" * 60)

# if __name__ == "__main__":
#     # Assumes the log is in the same folder
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     log_file_path = os.path.join(script_dir, "server_traffic.log")
    
#     parse_logs(log_file_path)


import os

# ANSI Color Codes
RED = '\033[91m'
RESET = '\033[0m'

def analyze_port_risk(port):
    """Provides a specific action plan based on the targeted port."""
    if port == "22":
        print(f"{RED}[!] SSH Attack Detected: Change passwords and enable SSH-Keys.{RESET}")
    elif port == "445":
        print(f"{RED}[!] RANSOMWARE PATTERN: Isolate system and check backups!{RESET}")

def parse_logs(log_file):
    failed_ips = {}
    failed_users = {}
    threshold = 2

    if not os.path.exists(log_file):
        print(f"Error: {log_file} not found.")
        return

    with open(log_file, 'r') as f:
        print("\n--- ANALYZING SECURITY LOGS ---")
        for line in f:
            if "Unauthorized access attempt on port" in line:
                port = line.split("port")[-1].strip()
                analyze_port_risk(port)

            if "Failed login" in line:
                try:
                    ip = line.split("from")[-1].strip()
                    user = line.split("user")[-1].split("'")[1]
                    failed_ips[ip] = failed_ips.get(ip, 0) + 1
                    failed_users[user] = failed_users.get(user, 0) + 1
                except:
                    continue

    print("\n" + "="*50)
    print("INCIDENT SUMMARY")
    print("="*50)
    for ip, count in failed_ips.items():
        if count > threshold:
            print(f"BRUTE FORCE: IP {ip} failed {count} times.")
    for user, count in failed_users.items():
        if count > threshold:
            print(f"{RED}TARGETED ACCOUNT: '{user}' attacked {count} times.{RESET}")
    print("="*50)