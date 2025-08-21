import os
import json
from .auth import verifica_master


BASE_DIR = os.path.dirname(
          os.path.abspath(
              os.path.join(os.path.dirname(__file__), "../")
          )
)

PASSWORDS_FILE = os.path.join(BASE_DIR, "passwords.json")

if not os.path.exists(PASSWORDS_FILE):
    with open(PASSWORDS_FILE, "w", encoding="utf-8") as file:
        json.dump([], file)

def carica_dati():
    try:
        with open(PASSWORDS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def salva_dati(dati):
    with open (PASSWORDS_FILE, "w", encoding="utf-8") as file:
        json.dump(dati, file, indent=4, ensure_ascii=False)

def aggiungipassword():
    dati=carica_dati()
        
    sito=input("Inserisci il nome del sito: ")
    username=input("Inserisci username/email da salvare: ")
    password=input("Inserisci la password da salvare: ")

    dati.append({
        "sito": sito,
        "username": username,
        "password": password
    })

    salva_dati(dati)
    print("Password salvata con successo")

def rimuovipassword():
    dati=carica_dati()
    if not dati:
        print("Non ci sono password da rimuovere")
        return

    print("\nPasswords salvate: ")
    for i, entry in enumerate(dati, start=1):
        print(f"{i}. Sito:{entry.get('sito', 'non presente')}, username:{entry.get('username', 'non presente')}")

    scelta=int(input("Inserisci il numero della password da eliminare: "))
    if scelta < 1 or scelta > len(dati):
        print("Numero inserito non valido")
        return
    password_rimossa=dati.pop(scelta - 1)
    salva_dati(dati)
    print(f"Password per il sito '{password_rimossa.get('sito','')} rimossa con successo")
    return

def visualizzapassword():
    print("Queste sono tutte le tue password: ")
    dati=carica_dati()
    for i, entry in enumerate(dati, start=1):
        print(f"{i}. {entry}")

    
def uscitaprogramma():
    while True:
        scelta=input("Inserisce la lettera ('e') per uscire dal programma o la lettera ('b') per tornare al menù -> ")
        if scelta=="e":
            exit(0)
        elif scelta=="b":
                return
        else:
            print("Comando non valido, riprovare.")        

def menu():

    verifica_master()

    while True:
        print("\n===Localpwd Password Manager===")
        
        print("1. Aggiungi password")
        print("2. Rimuovi password")
        print("3. Visualizza passwords")
        print("4. Esci dal programma")
        scelta=input("Seleziona un'opzione (1-4): ").strip()
        if scelta == "1":
            aggiungipassword()
        elif scelta == "2":
            rimuovipassword()
        elif scelta == "3":
            visualizzapassword()
        elif scelta == "4":
            uscitaprogramma()
        else:
            print("Opzione non valida.")
