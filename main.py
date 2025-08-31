# Corelogic access
import sys
import os

# add SRC folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# import menu func
from localpwd.corelogic import menu

if __name__ == "__main__":
    menu()
