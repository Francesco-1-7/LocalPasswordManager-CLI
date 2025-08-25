import getpass
import hashlib
import json
import os
import sys

MASTER_FILE = "Master.json"
ITERAZIONI = 100_000
LUNGHEZZA_CHIAVE = 32

def genera_salt():
    return os.urandom(16)

def deriva_chiave(master, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        master.encode(),
        salt,
        ITERAZIONI,
        dklen=LUNGHEZZA_CHIAVE
    ).hex()

def imposta_master():
    while True:
        master = getpass.getpass("Inserisci la tua nuova master password: ")
        conferma = getpass.getpass("Conferma la password inserita: ")
        if conferma != master:
            print("Password non corrisponde, riprova")
            continue

        salt = genera_salt()
        chiave = deriva_chiave(master, salt)
        dati = {
            "salt": salt.hex(),
            "hash": chiave
        }

        with open(MASTER_FILE, "w") as file:
            json.dump(dati, file)

        print("Master password impostata correttamente")
        return master

def verifica_master():
    if not os.path.exists(MASTER_FILE):
        print("Non esiste una master password, aggiungila di seguito: ")
        return imposta_master()

    with open(MASTER_FILE, "r") as file:
        dati = json.load(file)

    salt = bytes.fromhex(dati["salt"])
    hash_salvato = dati["hash"]

    for _ in range(3):
        master = getpass.getpass("Inserisci la master password: ")
        chiave = deriva_chiave(master, salt)
        if chiave == hash_salvato:
            print("Accesso consentito")
            return master
        else:
            print("Master password errata")

    print("Troppi tentativi falliti, uscita dal programma")
    sys.exit()
