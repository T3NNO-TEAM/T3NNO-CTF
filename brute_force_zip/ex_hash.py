from zipfile import ZipFile
from pathlib import Path
from multiprocessing import Pool, cpu_count
from colorama import Fore, init
from ExtractFiles.ExtractAllFiles import Extract


init()

class BruteForseZip:
    def __init__(self):
        self.brute_forse()
        
    def extract_all(self, pwd_):
        try:
            with Extract(path_file) as file:
                file.extractall(pwd=pwd_.encode())
                return pwd_
        except KeyError:
            return False
        
    def brute_forse(self):
        global path_file
        limit = 0
        while limit != 5:
            try:
                path_file = "/home/dalas/droidcam/hello.zip"#input('enter the path file zip >> ')
                wordlist_path = "/home/dalas/Downloads/ss/n.txt"#input('enter the path wordlist >> ')
            except KeyboardInterrupt:
                continue
            
            
            if not path_file or not wordlist_path:
                limit += 1
                continue
                
            if not Path(path_file).exists():
                print(f"[-] The {path_file} Not fond")
                limit += 1
                continue
            
            if not Path(wordlist_path).exists():
                print(f"[-] The {wordlist_path} Not fond")
                limit += 1
                continue
            
            
            with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as pas:
                passwords = [p.strip() for p in pas]
            
            task = ((passw) for passw in passwords)
            
            
            with Pool(cpu_count()-2) as pool:
                for result in pool.imap_unordered(self.extract_all, task, chunksize=500):
                    print(result)
                    if result:
                        
                        pool.terminate()
                        print("[+] The password is {}".format(result))
                        
                        
            break
        print(Fore.LIGHTGREEN_EX+"[-]"+Fore.LIGHTWHITE_EX+" Pless Change Wordlist ")
BruteForseZip()