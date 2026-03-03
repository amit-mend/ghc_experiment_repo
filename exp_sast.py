import hashlib
import random
import subprocess

# Low severity: Use of weak but non-critical hash (MD5)
def generate_file_checksum(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# Low severity: Use of random instead of secrets for non-security token
def generate_session_token():
    token = random.randint(100000, 999999)
    return str(token)


# Low severity: Hardcoded debug flag / magic string
DEBUG_MODE = True
APP_VERSION = "1.0.0"


# Low severity: Print statement exposing non-sensitive internal info
def get_user_info(user_id):
    print(f"Fetching user with ID: {user_id}")
    return {"id": user_id, "name": "Test User"}


# Low severity: Unused import / dead code (flagged by some SAST tools)
def legacy_ping(host):
    result = subprocess.run(["ping", "-c", "1", host], capture_output=True)
    return result.returncode == 0


if __name__ == "__main__":
    checksum = generate_file_checksum("example.txt")
    print(f"Checksum: {checksum}")

    token = generate_session_token()
    print(f"Token: {token}")

    user = get_user_info(42)
    print(user)
