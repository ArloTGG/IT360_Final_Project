import os
import hashlib
from cryptography.fernet import Fernet
from datetime import datetime

# --- CONFIGURATION ---
LOG_SOURCE = "/var/log/audit/audit.log"
ENCRYPTED_OUTPUT_DIR = "/var/secure_logs/encrypted/"
KEY_FILE = "/var/secure_logs/secret.key"
# ---------------------

def load_or_generate_key():
    """Loads the existing encryption key or creates a new one."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        print(f"[!] No key found. Generating new key at {KEY_FILE}")
        key = Fernet.generate_key()
        os.makedirs(os.path.dirname(KEY_FILE), exist_ok=True)
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        # Restrict permissions to the key file
        os.chmod(KEY_FILE, 0o600)
        return key

def process_logs():
    if not os.path.exists(LOG_SOURCE):
        print(f"[-] Error: {LOG_SOURCE} not found. Is auditd running?")
        return

    # 1. Initialize Encryption
    key = load_or_generate_key()
    fernet = Fernet(key)

    # 2. Read the raw log data
    with open(LOG_SOURCE, "rb") as f:
        raw_data = f.read()

    if not raw_data:
        print("[*] Log file is empty. Nothing to do.")
        return

    # 3. Generate SHA-256 Hash for Integrity
    log_hash = hashlib.sha256(raw_data).hexdigest()
    
    # 4. Encrypt the data
    encrypted_data = fernet.encrypt(raw_data)

    # 5. Save the result
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"audit_log_{timestamp}.enc"
    output_path = os.path.join(ENCRYPTED_OUTPUT_DIR, output_filename)

    os.makedirs(ENCRYPTED_OUTPUT_DIR, exist_ok=True)
    
    with open(output_path, "wb") as f:
        # We store the hash at the top of the file for later verification
        f.write(f"HASH:{log_hash}\n".encode())
        f.write(encrypted_data)

    print(f"[+] Success!")
    print(f"    - Encrypted log: {output_path}")
    print(f"    - SHA-256 Hash: {log_hash}")

if __name__ == "__main__":
    # Ensure script is run with high enough privileges to read /var/log/audit/
    if os.geteuid() != 0:
        print("[-] This script must be run as root/sudo to access audit logs.")
    else:
        process_logs()
