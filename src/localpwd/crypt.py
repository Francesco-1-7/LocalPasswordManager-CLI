#Qui utilizzeremo il codice per la cifratura delle passwords
import base64
import hashlib
from cryptography.fernet import Fernet

def derive_key(masterpassword): #Chiave derivata dalla master, usata per cifrare le passwords
    masterpassword_bytes = masterpassword.encode()
    hashed_password = hashlib.sha256(masterpassword_bytes)
    digest_bytes = hashed_password.digest()
    key = base64.urlsafe_b64encode(digest_bytes)
    return key

def encrypt_password(password, masterpassword): #cifratura
    key = derive_key(masterpassword)
    fernet_cipher = Fernet(key)
    password_bytes = password.encode()
    encrypted_bytes = fernet_cipher.encrypt(password_bytes)
    encrypted_string = encrypted_bytes.decode()
    return encrypted_string

def decrypt_password(token, masterpassword): #decifratura
    key = derive_key(masterpassword)
    fernet_cipher = Fernet(key)
    token_bytes = token.encode()
    decrypted_bytes = fernet_cipher.decrypt(token_bytes)
    decrypted_string = decrypted_bytes.decode()
    return decrypted_string