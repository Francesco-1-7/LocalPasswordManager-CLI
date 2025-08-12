import json

def aggiungipassword():
    with open("passwords.json", "r", encoding="utf-8") as file:
        dati=json.load(file)
        
    sito=input("Inserisci il nome del sito: ")
    username=input("Inserisci username/email da salvare: ")
    password=input("Inserisci la password da salvare: ")

    dati.append({
        "sito": sito,
        "username": username,
        "password": password
    })

    with open("passwords.json", "w", encoding="utf-8") as file:
        json.dump(dati, file, indent=4, ensure_ascii=False)

    print("Password salvata con successo")

def menu():
    while True:
        print("\n===Localpwd Password Manager===")
        
        print("1. Aggiungi una nuova password")
        print("2. Visualizza le password salvate")
        print("3. Esci da Localpwd")
        scelta=input("Seleziona un'opzione (1-3): ").strip()
        if scelta == "1":
            aggiungipassword()