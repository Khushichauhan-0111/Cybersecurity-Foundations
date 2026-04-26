import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def check_integrity(file_path, baseline_path):
    if not os.path.exists(baseline_path):
        print("[!] No baseline found. Creating new baseline...")
        with open(baseline_path, "w") as f:
            f.write(calculate_hash(file_path))
        print("[+] Baseline created successfully.")
        return

    with open(baseline_path, "r") as f:
        stored_hash = f.read()

    current_hash = calculate_hash(file_path)

    if current_hash == stored_hash:
        print(f"[OK] {file_path} is intact.")
    else:
        print(f"[ALERT] {file_path} has been MODIFIED!")
        print(f"Expected: {stored_hash}")
        print(f"Actual:   {current_hash}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_to_watch = os.path.join(script_dir, "system_config.txt")
    baseline = os.path.join(script_dir, "baseline.txt")

    if not os.path.exists(file_to_watch):
        with open(file_to_watch, "w") as f:
            f.write("SECRET_KEY=123456")
        print(f"[+] Created {file_to_watch} for monitoring.")

    check_integrity(file_to_watch, baseline)