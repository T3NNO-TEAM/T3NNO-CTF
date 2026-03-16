from pathlib import Path
import hashlib
from colorama import Fore, init
from multiprocessing import Pool, cpu_count
from Hash_Checker.hash_chcker import  hash_checker

init()

class BruteForcFile:
    def __init__(self):
        self.main()
        
    def hashing_pwd(self, args):
        algo, text = args
        try:
            h = hashlib.new(algo)
            h.update(text.encode())
            return h.hexdigest(), text
        except Exception:
            return None

    def brud_fors(self, hash_target, wordlist_path):

        hash_list = hash_checker(hash_target)

        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [p.strip() for p in f]

        for algo in hash_list:

            tasks = ((algo, pwd) for pwd in passwords)
            
            with Pool(cpu_count()) as pool:
                for result in pool.imap_unordered(self.hashing_pwd, tasks, chunksize=500):

                    if result is None:
                        continue

                    result_hash, pwd = result

                    if result_hash == hash_target:
                        pool.terminate()
                        print("FOUND:", pwd)
                        return

        print("Not found hash")
        

    def main(self):
        limit = 0
        while limit != 5:
            try:
                target_hash = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"#input(Fore.BLACK+"[+]"+Fore.LIGHTWHITE_EX+" Enter the target >> ")#"4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2"
                if not target_hash:
                    limit+=1
                    continue
                wordlist_path = "/home/dalas/Downloads/ss/n.txt"#input(Fore.BLACK+"[+]"+Fore.LIGHTWHITE_EX+"Enter The Word List Path >> ") #"/home/dalas/Downloads/ss/rockyou.txt" '/home/dalas/Downloads/ss/rockyou.txt' 
                if not wordlist_path:
                    limit += 1
                    continue
            except KeyboardInterrupt:
                print('\n')
                limit+=1
                continue
            
            
            
            if not Path(wordlist_path).exists():
                limit += 1
                continue
            
            self.brud_fors(target_hash, wordlist_path)
            
            break

if __name__ == '__main__':
    pass