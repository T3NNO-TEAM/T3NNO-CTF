import sys
import threading
from colorama import Fore, init
from file_scanner.files_scan import FileScaner
from forms_scanner.forms_scan import FormsScan
from web_scaner.xss_chcker.xss_scan import XssScanner

init()



def web_scanner():
    global tor_proxy
    print(
"""    
[1] Full Scaner 
[2] Xss Scaner
[3] Form scan
[4] File Scan
    """
    )
    limit = 0
    while limit != 5:
        try:
            option = int(input("Select option : "))
        except ValueError:
            limit += 1
            print(Fore.LIGHTGREEN_EX+"\n[-]"+Fore.LIGHTWHITE_EX+" Pless Enter a Number")
            continue
        
        except KeyboardInterrupt:
            print(Fore.LIGHTGREEN_EX+"\n[-]"+Fore.LIGHTWHITE_EX+"If Wanna Exit Press Key 'exit' OR 'No' >> ")
           
                
            if check_except == "exit":
                sys.exit(0)
            else:
                continue
        
        if not option:
            print(Fore.LIGHTRED_EX+"[-]"+Fore.LIGHTWHITE_EX+" Pless Enter The Target 'URL'")
            limit+=1
            continue
        
        if option == 1:
            # function full scan
            async def full_scan(target_url):
                file_scanner =  FileScaner()
                file_scanner.files_scan(target_url)
                form_scanner = FormsScan()
                form_scanner.forms_scan(target_url)
                xss_scanner = XssScanner()
                xss_scanner.xss_scan(target_url)
                
            try:
                target = input(Fore.BLACK+"\n[+]"+Fore.LIGHTWHITE_EX+"Enter The Target 'URL' 'http://expoim.com' >> ")
            except KeyboardInterrupt:
                try:
                    check_except = input(Fore.LIGHTGREEN_EX+"\n[-]"+Fore.LIGHTWHITE_EX+"If Wanna Exit Press Key 'exit' OR 'No' >> ").lower().strip()
                except KeyboardInterrupt:
                    sys.exit(0)
                    
                if check_except == "exit":
                    sys.exit(0)
            full_scan()
            
        elif option == 2:
            XssScanner.main()
        
        elif option == 3:
            FormsScan.main()
        
        elif option == 4:
            FileScaner.main()
    
web_scanner()