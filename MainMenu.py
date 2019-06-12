import os
import time
import subprocess


loop = ''
choice = ''
menu = """
############################################
############################################
####              Main Menu             ####	
####        1. Fortigate Operations     ####
####        2. Nomadix Operations       ####
####        3. Marqui port Matrix       ####
####        4. Nmap Target              ####
####        5. MTR Target               ####
####        6. Passwords                ####
####        7. AGS Operations           ####
############################################
######################R.DiMaggio############
			"""

def mainMenu():
	os.system('cls')
	global choice
	print(menu)
	choice = input("Select an operation to perform... \n")
	os.system('cls')

mainMenu()
while loop == 'yes' or 'y':
	os.system('cls')
	if choice == '1':
		subprocess.call("FortiINFO.py", shell=True)
		mainMenu()
	elif choice == '2':
		subprocess.call("SNMPNomNom.py", shell=True)
		loop = input("Return to menu? \n")
		mainMenu()
	elif choice == '3':
		subprocess.call("MarquiPorts.py", shell=True)
		loop = input("Return to menu? \n")
		mainMenu()
	elif choice == '4':
		subprocess.call("TODO", shell=True)
		loop = input("Return to menu? \n")
		mainMenu()
	elif choice == '5':
		subprocess.call("TODO", shell=True)
		loop = input("Return to menu? \n")
		mainMenu()
	elif choice == '6':
		subprocess.call("passwords.py", shell=True)
		mainMenu()
	elif choice == '7':
		subprocess.call("AGS.py", shell=True)
		mainMenu()
	else:
		print(choice)
		print("Invalid choice...")
		loop = input("Return to menu? \n")
		mainMenu()