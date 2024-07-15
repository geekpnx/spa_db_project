
import os
from deco.spa_db_banner import spa_banner

banner = spa_banner()
DASH = 15*'-'

#========= UNDER CONSTRUCTION ========

def under_construction():
    os.system('clear')
    print(f"{banner}\n\nThis option is not yet available")
    input("\nPress 'enter' to exit ...\n")
    os.system('clear')
