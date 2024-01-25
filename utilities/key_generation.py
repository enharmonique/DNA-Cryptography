import hashlib


def generate_secure_key(passphrase):
    # Use a cryptographic hash function (SHA-256) to generate a key from the passphrase
    hashed_passphrase = hashlib.sha256(passphrase.encode()).hexdigest()
    return hashed_passphrase