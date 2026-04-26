import os
import sys

# ANSI Colors for professional output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

# --- AUTOMATIC PATH LOCATOR ---
# This line finds the folder where this script (monitor.py) is actually saved
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# THE BASELINE (The Ground Truth)
BASELINES = {
    "healthcare.txt": {"DOSE": "5mg", "MEDICATION": "Insulin"},
    "inventory.txt": {"PRICE": "500", "STOCK": "10"},
    "legal.txt": {"TIMESTAMP": "14:00:05", "EVIDENCE": "Blood_Sample"}
}

def load_file_data(filename):
    """Constructs the absolute path and reads the file data."""
    # This combines the folder path with the filename
    file_path = os.path.join(SCRIPT_DIR, filename)
    
    data = {}
    if not os.path.exists(file_path):
        print(f"{RED}[!] FILE NOT FOUND: {file_path}{RESET}")
        return None
        
    with open(file_path, "r") as f:
        for line in f:
            if ":" in line:
                key, val = line.split(":", 1) # Split only on the first colon
                data[key.strip()] = val.strip()
    return data

def forensic_analysis(filename):
    print(f"\n{BLUE}[SCANNING] Checking Integrity of: {filename}...{RESET}")
    
    current_data = load_file_data(filename)
    if current_data is None:
        return

    baseline = BASELINES.get(filename)
    tampered = False

    for key, expected_val in baseline.items():
        actual_val = current_data.get(key)

        if actual_val != expected_val:
            tampered = True
            print(f"{RED}[!] ALERT: Unauthorized Modification Detected in {key}!{RESET}")
            print(f"    Expected: {expected_val}")
            print(f"    Actual:   {actual_val if actual_val else 'MISSING'}")

            # INDUSTRY SPECIFIC LOGIC
            if "DOSE" in key:
                print(f"{RED}    RISK: High probability of medical harm.{RESET}")
            elif "PRICE" in key:
                print(f"{YELLOW}    RISK: Financial fraud / Price manipulation.{RESET}")
            elif "TIMESTAMP" in key:
                print(f"{RED}    RISK: Legal evidence chain broken.{RESET}")

    if not tampered:
        print(f"{GREEN}[OK] File {filename} matches the secure baseline.{RESET}")

def run_suite():
    print("="*60)
    print("      FORENSIC MONITORING SYSTEM ")
    print("="*60)
    print(f"Target Directory: {SCRIPT_DIR}\n")
    
    for filename in BASELINES.keys():
        forensic_analysis(filename)
    
    print("\n" + "="*60)
    print("SCAN COMPLETE.")

if __name__ == "__main__":
    run_suite()