#!/usr/bin/python3

import sys
import os
import hashlib,time
from colorama import init,Fore,Back,Style

os.system("clear")

"""--------------------------------------COLOR_BRIGHT---------------------"""
GREEN = Fore.GREEN+Style.BRIGHT
RED = Fore.RED+Style.BRIGHT
BLACK = Fore.BLACK+Style.BRIGHT
WHITE = Fore.WHITE+Style.BRIGHT
YELLOW = Fore.YELLOW+Style.BRIGHT
BLUE = Fore.BLUE+Style.BRIGHT
RESET = Style.RESET_ALL
"""--------------------------------------COLOR_DIM-------------------------"""
D_GREEN = Fore.GREEN+Style.DIM
D_RED = Fore.RED+Style.DIM
D_BLACK = Fore.BLACK+Style.DIM
D_WHITE = Fore.WHITE+Style.DIM
D_BLUE = Fore.BLUE+Style.DIM
D_YELLOW = Fore.YELLOW+Style.DIM

"""------------------------------------------------LOGO---------------------------------------------"""

hash_G=f"""{BLUE}
		─┼─┼─  ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐LINUX
		─┼─┼─  ║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
		       ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─
		        CODED BY SAURABH WADEKAR 
"""


"""---------------------------------------HASH GENRETOR------------------------------"""
def Hash_Generator():
	os.system("clear")
	print(hash_G)
	hash_input = input(RED+"Enter Srings >"+RESET)
	hash_md5 = hashlib.md5(hash_input.encode('utf-8'))
	hash_sha1 = hashlib.sha1(hash_input.encode('utf-8'))
	hash_sha224 = hashlib.sha224(hash_input.encode('utf-8'))
	hash_sha256 = hashlib.sha256(hash_input.encode('utf-8'))
	hash_sha384 = hashlib.sha384(hash_input.encode('utf-8'))
	hash_sha512 = hashlib.sha512(hash_input.encode('utf-8'))
	hash_blake2b = hashlib.blake2b(hash_input.encode('utf-8'))
	hash_blake2s = hashlib.blake2s(hash_input.encode('utf-8'))

	if hash_input == "":
		print(f"{D_RED}Invali Sring{RESET}")
		time.sleep(1)
		Hash_Generator()
	else:
		os.system("clear")
		print(hash_G)
		print("")
		print(f"	     {RED}Sring :{RED} [  {GREEN}{hash_input}{RED}  ]{RESET}")
		print("")
		print(RED+"[+]"+BLUE+" MD5    : "+RED+"[ "+D_BLUE,str(hash_md5.hexdigest()),RED," ]",RESET)
		print(RED+"[+]"+BLUE+" SHA1   : "+RED+"[ "+D_BLUE,str(hash_sha1.hexdigest()),RED," ]",RESET)
		print(RED+"[+]"+BLUE+" SHA224 : "+RED+"[ "+D_BLUE,str(hash_sha224.hexdigest()),RED," ]",RESET)
		print(RED+"[+]"+BLUE+" SHA256 : "+RED+"[ "+D_BLUE,str(hash_sha256.hexdigest()),RED," ]",RESET)
		print(RED+"[+]"+BLUE+" SHA384 : "+RED+"[ "+D_BLUE,str(hash_sha384.hexdigest()),RED," ]",RESET)
		print(RED+"[+]"+BLUE+" SHA512 : "+RED+"[ "+D_BLUE,str(hash_sha512.hexdigest()),RED," ]",RESET)
		print(RED+"[+]"+BLUE+" BLAKE2B: "+RED+"[ "+D_BLUE,str(hash_blake2b.hexdigest()),RED," ]",RESET)
		print(RED+"[+]"+BLUE+" BLAKE2S: "+RED+"[ "+D_BLUE,str(hash_blake2s.hexdigest()),RED," ]",RESET)
		print("\n")
		input(RED+"["+GREEN+"Press Enter To Back"+RED+"]"+RESET)
		Hash_Generator()


"""----------------------------------------------------------------------------------"""


Hash_Generator()
