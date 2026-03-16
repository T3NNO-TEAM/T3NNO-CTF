from bs4 import BeautifulSoup
import requests
import sys
import random
import os
from pathlib import Path
from colorama import Fore, init
from web_scaner.Header import user_agent_list

init()

TOR_PROXY = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

class FormsScan:
        
    def request(self, url):
        try:
            return requests.get(
                url, 
                headers={"User-Agent":''.join(random.choice(user_agent_list))},
                proxies=TOR_PROXY
                )
        except Exception:
            return None
    
    def forms_scan(self, target_url):
      
        response = self.request(target_url)

        if response and response.status_code == 200:
            parsed_html = BeautifulSoup(response.content, "html.parser")
            forms_list = parsed_html.find_all("form")
            if forms_list:
                folder_result = os.path.join(Path.home(), "Desktop", "result", "FormScaner")
                os.makedirs(folder_result, exist_ok=True)
                    
                for form in forms_list:
                    
                    with open(os.path.join(folder_result, "result_forms.txt"), "a", encoding='utf-8', errors='ignore') as result_file:
                        result_file.write(str(form))
                
                print(Fore.BLACK+"[+]"+Fore.LIGHTWHITE_EX+" Result Path: {}".format(folder_result))
            
        else:
            print(Fore.LIGHTRED_EX+"[-]"+Fore.LIGHTWHITE_EX+" No response from target")
    
    def main(self):
        limit = 0
        while limit != 5:
            try:
                target_url = input(Fore.BLACK+"\n[-]"+Fore.LIGHTWHITE_EX+"Enter The Target 'URL' 'http://expoim.com'>> ")
            except KeyboardInterrupt:
                print(Fore.LIGHTGREEN_EX+"\n[*]"+Fore.LIGHTWHITE_EX+"exit from Tenno CTF TOOL ")
                sys.exit(0)
                
            if not target_url:
                print(Fore.LIGHTRED_EX+"[-]"+Fore.LIGHTWHITE_EX+"Pless Enter The 'URL'")
                limit+=1
                continue
            self.forms_scan(target_url)
            break

if __name__ == "__main__":
    done = FormsScan()
    done.main()