import requests
import os
import random
import asyncio
from colorama import Fore, init
from pathlib import Path
from urllib.parse import urlparse
from file_scanner.allfile import paths
from Header import user_agent_list

init()

class FileScaner:
  
    async def send_req(self, url):
        
        try:
            return requests.get(url, headers={"User-Agent":random.choice(user_agent_list)}, timeout=5)
        except requests.exceptions.RequestException:
            return None

    def files_scan(self, target_url):
        result_url = []
        try:

            for line in paths:
                test_url = f"{target_url}/{line.strip()}"

                respons = asyncio.run(self.send_req(test_url))
                
                if not respons:
                    continue
                
                if respons.status_code == 200:
                    print(Fore.LIGHTGREEN_EX + test_url)
                    result_url.append(test_url)
                
            if result_url:
                result_folder = os.path.join(Path.home(), 'Desktop', "result", "FileScaner")
                os.makedirs(result_folder, exist_ok=True)

                with open(os.path.join(result_folder, f"{urlparse(target_url).netloc}_result.txt"), "w", encoding='utf-8', errors='ignore') as file_json:
                    file_json.write("\n".join(str(x) for x in result_url))
                        
                        
        except FileNotFoundError as e:
            print(f"[!] File not found: {e}")
                
    def main(self):
        import sys
        
        limit = 0
        while limit != 5:
            try:
                target_url = input(Fore.LIGHTBLACK_EX+"\n[+]"+Fore.LIGHTWHITE_EX+" Enter The Target 'URL OR IP' >> ")
            except KeyboardInterrupt:
                try:
                    check_except = input(Fore.LIGHTGREEN_EX+"\n[-]"+Fore.LIGHTWHITE_EX+"If Wanna Exit Press Key 'exit' OR 'No' >> ").lower().strip()
                except KeyboardInterrupt:
                    sys.exit(0)
                if check_except == "exit":
                    sys.exit(0)
                else:
                    continue
            
            if not target_url:
                print(Fore.LIGHTRED_EX+"[-]"+Fore.LIGHTWHITE_EX+"Pless Enter The 'URL OR IP'")
                limit+=1
                continue
            
            self.files_scan(target_url)
            break

done = FileScaner()
done.main()