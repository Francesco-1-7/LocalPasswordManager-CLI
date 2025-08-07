# Localpwd

This is a simple and secure command-line password manager written in Python.  
It is designed for secure credential management via encrypted local storage and is completely offline.
Future updates will include a GUI.

## ✅ Features

- View, add, edit, and delete credentials
- Master password protection
- Encrypted local storage
- Fully offline
- Clean CLI menu interface
- Modular code, easy to extend

## 🚀 Installation

> ⚠️ Requires **Python 3.10 or higher**

Clone the repository, install the dependencies, run the program:

- Clone the repository

```bash
git clone https://github.com/Francesco-1-7/Localpwd.git
cd Localpwd
```
- Install dependencies 

```bash
pip install -r requirements.txt
```

- Run the program

```bash
python main.py
```
---
## 🔐 Security
*Passwords are stored encrypted locally*

*A master password is required to access the vault*

*No data is sent over the network*

---
## 📁 Project Structure
```bash
Copia
Modifica
Localpwd/
├── core/              # Logica dell'applicazione
│   └── ...
├── data/              # Vault criptato
├── utils/             # Funzioni di supporto
├── main.py            # Entry point
├── requirements.txt   # Dipendenze Python
└── README.md
```
---
## 🛣️ Next steps
- GUI support (Tkinter / PyQt / other)

- Secure export/import

- Built-in password generator

- Encrypted activity logging

### 👨‍💻 Author
***Francesco Panarese***