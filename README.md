# Local Password Manager

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
## Run as Executable (Windows)

If you don't want to install Python, you can use the precompiled executable.

1. Download the latest `.exe` file from the [Releases](https://github.com/Francesco-1-7/LocalPasswordManager-CLI/releases) page.
2. Place it in any folder on your computer.
3. Run it by double-clicking
   
or from the terminal:
```bash
.\localpwd.exe
```

## 🔐 Security
*Passwords are stored encrypted locally*

*A master password is required to access the vault*

*No data is sent over the network*

---
## 📁 Project Structure
```bash

Localpwd/
├── src/               # App logic
│   └── localpwd
        __init__.py
        corelogic.py
        crypt.py
        auth.py 
├── License            
├── main.py            # Entry point
├── requirements.txt   # Python dependencies
└── README.md
```
---
## 🛣️ Next steps
- GUI support

- Secure export/import

- Built-in password generator

- Encrypted activity logging

---

### 👨‍💻 Author
***Francesco_1_7***
