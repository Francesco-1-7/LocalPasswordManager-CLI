# Iniziamo a scrivere la logica del password manager

def menu():
    while True:
        print("\n===Localpwd Password Manager")
        print("1. Aggiungi una nuova password")
        print("2. Visualizza le password salvate")
        print("3. Esci da Localpwd")

        scelta=input("Seleziona un'opzione (1-3): ").strip()

        if scelta == "1":
            print("Funzione aggiunta password (da implementare)")
        elif scelta == "2":
            print("Funzione visualizza password (da implementare)")
        elif scelta == "3":
            print("Uscita in corso...")
            break
        else:
            print("Opzione non valida. Riprova.")
