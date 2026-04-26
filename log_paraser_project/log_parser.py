import os
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
