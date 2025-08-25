# Accesso al corelogic

import sys
import os

# Aggiunge la cartella "src" al path dei moduli
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# Importa la funzione menu dal tuo modulo
from localpwd.corelogic import menu

if __name__ == "__main__":
    menu()