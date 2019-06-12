import os
import pyperclip

supportPass = "PasswordX"
suPass = "PasswordZ"

pMenu = """
############################################
############################################
####              Passwords             ####	
####        1. support/eth              ####
####        2. super user/eth           ####
####        3. DCI                      ####
############################################
######################R.DiMaggio############
			"""
print(pMenu)
choice = input("select password to clip \n")

if choice == '1':
	pyperclip.copy(supportPass)
elif choice == '2':
	pyperclip.copy(suPass)
else:
	print("Invalid choice...")