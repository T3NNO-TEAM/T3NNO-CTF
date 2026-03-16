from scapy.all import *
from colorama import Fore, init
import threading



class PortScaner:
    def __init__(self):
        self.main()
        
    def __port_scaner__(self, target_ip, port):
        
        try:
            packge = IP(dst=target_ip)/TCP(dport=port, flags="S")
            respons = sr1(packge, timeout=0.5, verbose=0)
            if respons and respons.haslayer(TCP):
                if respons[TCP].flags == 0x12:
                    print(f"Port Open {port}")

        except OSError:
            return
        
        except PermissionError as e:
            import sys
            
            print(f"[-] Permisson Error {e}")
            sys.exit(0)
            
    def main(self):
        limit = 0
        while limit != 5:
            try:
                target_ip = input(Fore.BLACK+"[+]"+Fore.LIGHTWHITE_EX+"Enter The Target IP >> ").strip()
            except KeyboardInterrupt as e:
                print(f"\n{e}\n")
                limit+=1
                continue
            
            if target_ip:
                for port in range(1, 1001):
                    t = threading.Thread(target=self.__port_scaner__, args=(target_ip, port))
                    t.start()
            else:
                limit += 1
                continue