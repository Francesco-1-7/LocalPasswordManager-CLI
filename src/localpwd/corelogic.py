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

def rimuovipassword():
    with open("passwords.json", "r",encoding="utf-8") as file:
        dati=json.load(file)
    if not dati:
        print("Non ci sono password da rimuovere")
    
    print("\nPasswords salvate: ")
    for i, entry in enumerate(dati):
        print(f"{i}: Sito:{entry.get('sito', '')}, username:{entry.get('username', '')}")
    try:
        indice=int(input("Inserisci il numero della password da eliminare (lista parte da 0): "))
        if 0 <= indice < len(dati):
            rimossa=dati.pop(indice)
            with open("passwords.json", "w", encoding="utf-8") as file:
                json.dump(dati, file, indent=4, ensure_ascii=False)

            print(f"Password per il sito '{rimossa.get('sito','')}")
        else:
            print("Indice non valido")
    except ValueError:
        print("Devi inserire un numero valido")

    
def menu():
    while True:
        print("\n===Localpwd Password Manager===")
        
        print("1. Aggiungi una nuova password")
        print("2. Visualizza le password salvate")
        print("3. Esci da Localpwd")
        scelta=input("Seleziona un'opzione (1-3): ").strip()
        if scelta == "1":
            aggiungipassword()
        if scelta == "2":
            rimuovipassword()
        if scelta == "3":
            visualizzapassword()
        if scelta == "4":
            uscitaprogramma()