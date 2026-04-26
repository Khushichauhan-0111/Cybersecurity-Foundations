import getpass
import sys
import os
STORED_USER = "admin"
STORED_PASS = "TrustLab2026"
STORED_CODEWORD = "I am the one who knocks" 
def secure_login():
    attempts = 0
    while attempts < 3:
        print("\n" + "="*40)
        print("      NATIONAL SECURITY TERMINAL")
        print("="*40)
        
        user = input("Username: ")
        password = getpass.getpass("Password: ")

        if user == STORED_USER and password == STORED_PASS:
            print("\n[+] Primary Identity Verified.")
            passkey = getpass.getpass("Enter Secret Codeword: ")

            if passkey == STORED_CODEWORD:
                print("\n[SUCCESS] Welcome, Authorized User.")
                return True
            else:
                attempts += 1
                print(f"\n[!] INVALID CODEWORD. Attempts left: {3 - attempts}")
        else:
            attempts += 1
            print(f"\n[!] ACCESS DENIED. Attempts left: {3 - attempts}")

    print("\n[CRITICAL] Multiple failed attempts. System Lockdown initiated.")
    return False

if __name__ == "__main__":
    if secure_login():
        print("\n--- SECURITY MENU ---")
        print("1. Run Network Port Scanner")
        print("2. Analyze Security Logs")
        choice = input("\nSelect an option: ")
        if choice == '1':
            import port_scanner_revised
            port_scanner_revised.run_scanner()
        elif choice == '2':
            import log_parser 
            log_parser.parse_logs("server_traffic.log")
    else:
        sys.exit()
