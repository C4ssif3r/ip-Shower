import os
os.system("pip install socket")
os.system("pip install requests")
os.system("pip install colorama")
os.system("pip install time")
os.system("clear")
#_________________.
import requests
import time
import socket
import colorama
from colorama import Fore, init
import sys
#//////

init()

print (Fore.GREEN+ """

 _                 ____  _   _  _____        _______ ____ 
(_)_ __           / ___|| | | |/ _ \ \      / / ____|  _ \ 
| | '_ \   _____  \___ \| |_| | | | \ \ /\ / /|  _| | |_) | 
| | |_) | |_____|  ___) |  _  | |_| |\ V  V / | |___|  _ < 
|_| .__/          |____/|_| |_|\___/  \_/\_/  |_____|_| \_\ 
  |_| 

""")
print (Fore.BLUE+"""
METHODS: 

1 FOR GET IP LOCAL

2 FOR GET IP PUBLIC {Global ip}""")
print("")
print(Fore.GREEN+"")

get = input("""ENTER YOUR METHOD 1 or 2
>_ """)

if get == "1":

        hostname = socket.gethostname()

        ip_local = socket.gethostbyname(hostname)
        print (Fore.RED+"PLEASE WAIT ...")
        time.sleep(3.0)
        print (Fore.GREEN+"Your Local IP :",Fore.RED + ip_local)
#.....$.$.$.$..$_..$.$
if get == "2":
        print (Fore.RED+"PLEASE WAIT ...")
        time.sleep(3.0)
        public = requests.get("https://api.ipify.org").text
        print("")
        print("")
        time.sleep(3)
        print (Fore.GREEN+"Your public IP :",Fore.RED + public)
else:
        print (Fore.RED+'[×]'+Fore.YELLOW+' command invalid')
        input ('Press enter for exit')
        sys.exit()
         
