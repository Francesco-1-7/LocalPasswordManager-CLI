#Autenticazione Master 
import getpass
import hashlib
import json
import os
import sys

MASTER_FILE = "Master.json"

def imposta_master():
    while True:
        master=getpass.getpass("inserisci la tua nuova master password: ")
        conferma=getpass.getpass("conferma la password inserita: ")
        if conferma != master:
            print("Password non corrisponde, riprova")
            continue
        else:
            hash_master=hashlib.sha256(master.encode()).hexdigest()
            with open (MASTER_FILE, "w") as file:
                json.dump({"hash" : hash_master}, file)
            print("Master password impostata correttamente")
            return

def verifica_master():
    if not os.path.exists(MASTER_FILE):
        print("Non esiste una master password, aggiungila di seguito: ")
        imposta_master()

    with open (MASTER_FILE, "r") as file:
        dati=json.load(file)
        hash_salvato=dati["hash"]

    for _ in range (3):
        master=getpass.getpass("Inserisci la master password: ")
        hash_master=hashlib.sha256(master.encode()).hexdigest()
        if hash_master==hash_salvato:
            print("Accesso consentito")
            return True
        else:
            print("Master password errata")
    print("Troppi tentativi falliti, uscita dal programma")
    sys.exit()