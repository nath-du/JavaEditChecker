"""
Java Edit Checker

This module checks if a version of a Java file (jar) has been modified 
compared to a known version, using the SHA256 hash of the file. 
The known version is obtained from an external URL.

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ██████▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          ▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        ▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ██    ▒▒▒▒▒▒██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒      ▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          ▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒      ▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████      ▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒        ▒▒▒▒  ██▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒                ██▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          ▒▒▒▒▒▒        ██▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▒▒▒▒▒▒  ██▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓██        ▒▒▒▒▒▒▒▒▒▒      ██▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓██▓▓████▒▒▒▒▒▒    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒      ██▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓████▒▒▒▒▒▒▒▒      ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒██▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒        ██▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓██▒▒▒▒    ▒▒▒▒▒▒  ▒▒▒▒██▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓██▒▒████████████    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒            ▒▒▒▒██▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓██  ██▒▒▒▒▒▒▒▒██      ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██              ▒▒██▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓████▒▒▒▒▒▒▒▒  ████      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████        ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


"""

import hashlib
import time
import os
import sys
import requests
from colorama import init, Fore as cc

# Colors
init()
DR = R = cc.LIGHTRED_EX #red
G = cc.LIGHTGREEN_EX #green
C = cc.LIGHTCYAN_EX #cyan
Y = cc.LIGHTYELLOW_EX #yellow
W = cc.RESET #reset color

# Banner
banner = f'''
{G}
                                                                  
    __             _____   _ _ _          _           _           
 __|  |___ _ _ ___|   __|_| |_| |_    ___| |_ ___ ___| |_ ___ ___ 
|  |  | .'| | | .'|   __| . | |  _|  |  _|   | -_|  _| '_| -_|  _|
|_____|__,|\_/|__,|_____|___|_|_|    |___|_|_|___|___|_,_|___|_|    {G}~ {W}by Nath {G}~
                                                                  

{W}
'''

# Cls
def clear():
    "Function to clean the terminal"
    os.system('cls')

# Send request
SHA256V_URL = "https://pastebin.com/raw/pyur6emE"
DEC256V = requests.get(SHA256V_URL, timeout=10)

# Main
def main():
    print(banner)

    filename = input(f"[{Y}?{W}] Enter the path of the jar file (version): ")
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        file_sha256 = sha256_hash.hexdigest()
        print(f"[{C}!{W}] SHA256: ", file_sha256)

    print(f"[{C}!{W}] {C}Scanning... {W}")

    try:
        if file_sha256 in DEC256V.text:
            print(f"[{C}!{W}] {G}No Java Edit found, legit.")
            time.sleep(2)
            input(f"{W}Pess any key to perform another scan.")
            clear()
            main()
        else:
            print(f"[{C}!{W}] {R}Java Edit found, unlegit.")
            time.sleep(2)
            input(f"{W}Pess any key to perform another scan.")
            clear()
            main()
    except requests.Timeout:
        print(f"[{C}!{W}] Connection timed out. Please try again later.")
        time.sleep(10)
        sys.exit()

    print(f"{W}Press Enter to exit.")
    input()

if __name__ == "__main__":
    main()
