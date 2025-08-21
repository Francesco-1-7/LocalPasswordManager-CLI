#Qui utilizzeremo il codice per la cifratura delle passwords
import base64
import hashlib
from cryptography.fernet import Fernet

def derive_key(master_password):
    """
    Deriva una chiave Fernet dalla master password.
    """
    digest=hashlib.sha256(master_password.encode()).digest()
    key=base64.urlsafe_b64encode(digest)
    return key

def encrypt_password(password, master_password):
    """
    Cifra una password in chiaro con la master password.
    """
    key = derive_key(master_password)
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(token, master_password):
    """
    Decifra una password cifrata con la master password.
    """
    key = derive_key(master_password)
    f = Fernet(key)
    return f.decrypt(token.encode()).decode()