from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, DES
from Crypto.Random import get_random_bytes
import base64

# ================= RSA KEY GENERATION =================

def generate_keys():
    key = RSA.generate(2048)
    return key.publickey(), key

# ================= DES FUNCTIONS =================

def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

def des_encrypt(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded = pad(message)
    encrypted = cipher.encrypt(padded)
    return base64.b64encode(encrypted)

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(ciphertext))
    return decrypted.strip()

# ================= RSA FUNCTIONS =================

def rsa_encrypt(data, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(data)
    return base64.b64encode(encrypted)

def rsa_decrypt(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted = cipher.decrypt(base64.b64decode(ciphertext))
    return decrypted

# ================= HYBRID ENCRYPTION =================

def encrypt_message(message, public_key):

    # Random DES key
    des_key = get_random_bytes(8)

    # Encrypt message using DES
    encrypted_message = des_encrypt(message.encode(), des_key)

    # Encrypt DES key using RSA
    encrypted_key = rsa_encrypt(des_key, public_key)

    pgp_block = f"""
-----BEGIN PGP MESSAGE-----

Encrypted Key:
{encrypted_key.decode()}

Encrypted Data:
{encrypted_message.decode()}

-----END PGP MESSAGE-----
"""

    return pgp_block, encrypted_key, encrypted_message


def decrypt_message(enc_key, enc_msg, private_key):

    des_key = rsa_decrypt(enc_key, private_key)

    message = des_decrypt(enc_msg, des_key)

    return message.decode()

# ================= MAIN PROGRAM =================

print("Generating RSA Keys...")

public_key, private_key = generate_keys()

message = input("\nEnter message to encrypt: ")

pgp_block, enc_key, enc_msg = encrypt_message(message, public_key)

print("\n🔐 Encrypted PGP Block:")
print(pgp_block)

print("\nDecrypting Message...")

decrypted = decrypt_message(enc_key, enc_msg, private_key)

print("\nDecrypted Message:", decrypted)
