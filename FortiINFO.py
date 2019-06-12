import paramiko
import time
import os

fortiU = 'userX'
fortiP = 'PasswordX'
FortiHost = input("What is the IP of the Fortigate? \n")
menu = """
############################################
############################################
####              Fortigate             ####	
####        1. ARP List                 ####
####        2. MAC ADRR of FORTI        ####
####        3. Internal config          ####
####        4. WAN Config               ####
####        5. Routing Table            ####
############################################
######################R.DiMaggio############
			"""
print(menu)
fortiTask = input("Make your selection: \n")


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(FortiHost, port=22, username=fortiU, password=fortiP)
print("connections successful..")
time.sleep(.5)

if fortiTask == "1":
    stdin, stdout, stderr = ssh_client.exec_command("get system arp")
    output = stdout.readlines()
    time.sleep(.5)
    print("Grabbing arp table....")
    time.sleep(.5)
    with open("FortiARP.txt", "a") as file:
             file.write('\n'.join(output))
    print("ARP table write finished....")
elif fortiTask == "2":
    stdin, stdout, stderr = ssh_client.exec_command("get hardware nic internal1")
    output = stdout.readlines()
    time.sleep(.5)
    print("Grabbing MAC Addr....")
    time.sleep(.5)
    with open("FortiMAC.txt", "a") as file:
             file.write('\n'.join(output))
    print("Interface MAC ID write finished....")
elif fortiTask == "3":
    stdin, stdout, stderr = ssh_client.exec_command("show | grep -f internal")
    output = stdout.readlines()
    time.sleep(.5)
    print("Grabbing Internal Config....")
    time.sleep(.5)
    with open("Forti_Internal.txt", "a") as file:
             file.write('\n'.join(output))
    print("Backup successful....")
elif fortiTask == "4":
    stdin, stdout, stderr = ssh_client.exec_command("show | grep -f wan")
    output = stdout.readlines()
    time.sleep(.5)
    print("Grabbing WAN Config....")
    time.sleep(.5)
    with open("FortiARPList.txt", "a") as file:
             file.write('\n'.join(output))
    print("IP ARP list grab successful....")
elif fortiTask == "5":
    stdin, stdout, stderr = ssh_client.exec_command("get router info routing-table all")
    output = stdout.readlines()
    time.sleep(.5)
    print("Grabbing Routing Table....")
    time.sleep(.5)
    with open("RoutingTable.txt", "a") as file:
             file.write('\n'.join(output))
    print("Routing Table grab successful....")
else:
    print("..Invalid selection..")

time.sleep(1)
ssh_client.close()