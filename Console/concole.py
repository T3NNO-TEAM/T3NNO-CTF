import time
import sys
import random
from colorama import Fore, init
from rich.live import Live
from rich.console import Console
from rich.text import Text
from brute_force_hash.brute_force import BruteForsHash
from brute_force_zip.ex_hash import BruteForseZip
from port_scaner.PortScaner import PortScaner

init()

console = Console()

BANNER_RAW = """
    ______ _____ _   _ _   _  ____      ____ _____ _____ 
   /_  __/__  __/ | / / | / / __ \    / ___/_  __/ ___/ 
    / /    / / /  |/ /  |/ / / / /   / /    / / / __/   
   / /  __/ / / /|  / /|  / /_/ /   / /___ / / / /       TOOLS
  /_/  /____//_/ |_//_/ |_|____/    \____//_/ /_/       
"""

class AppConsole:

    def __init__(self):
        self.HomeAscii()

    def generate_glitch(self):

        chars = list(BANNER_RAW)

        for i in range(len(chars)):
            if chars[i] not in [" ", "\n"] and random.random() < 0.04:
                chars[i] = random.choice(["0", "1", "█", "░"])

        color = random.choice(
            ["bright_blue", "bright_green", "bright_red", "white"]
        )

        glitch_text = Text("".join(chars), style=color)

        status_msg = "\n   <<<< CTF tools t3nn0 t34m >>>>  : "

        return Text.assemble(glitch_text, status_msg)

    def HomeAscii(self):

        with Live(self.generate_glitch(), refresh_per_second=12, console=console) as live:

            for _ in range(60):
                time.sleep(0.08)
                live.update(self.generate_glitch())


if __name__ == '__main__':
    AppConsole()
    print("""
----------- menu -----------

[1] Brute Force Hash
[2] Brute Force ZipFile
[3] Port Scanner
[4] Web Scanner
[5] Get Files HASH
""")
    limit = 0
    while limit != 5:
        try:
            option = int(input("Select option : "))
        except ValueError:
            limit += 1
            print(Fore.LIGHTGREEN_EX+"\n[-]"+Fore.LIGHTWHITE_EX+" Pless Enter a Number")
            continue
        
        except KeyboardInterrupt:
            check_except = input(Fore.LIGHTGREEN_EX+"\n[-]"+Fore.LIGHTWHITE_EX+"If Wanna Exit Press Key 'exit' OR 'No' >> ").lower().strip()
            if check_except == "exit":
                sys.exit(0)
            else:
                continue
        
        if not option:
            print(Fore.LIGHTRED_EX+"[-]"+Fore.LIGHTWHITE_EX+" Pless Enter The Number")
            limit+=1
            continue
        
        if option == 1:
            BruteForsHash()
        elif option == 2:
            BruteForseZip()
        elif option == 3:
            PortScaner()
        