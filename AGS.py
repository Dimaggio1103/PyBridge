import paramiko
import time
import os

agsU = 'Userx'
agsP = 'PasswordX'
agsSP = 'PasswordZ'
agsHost = input("What is the VPN string of the AGS? \n")

dhcp = """clear_leases() {

   if [ -f /var/lib/dhcp/dhcpd.leases ]

   then

       /etc/init.d/isc-dhcp-server stop

       rm /var/lib/dhcp/dhcpd.leases

       touch /var/lib/dhcp/dhcpd.leases

       cleanroute.sh

       /etc/init.d/isc-dhcp-server start

   fi

   if [ -f /var/lib/dhcp3/dhcpd.leases ]

   then

       /etc/init.d/dhcp3-server stop

       rm /var/lib/dhcp3/dhcpd.leases

       touch /var/lib/dhcp3/dhcpd.leases

       cleanroute.sh

       /etc/init.d/dhcp3-server start

   fi

}"""


menu = """
############################################
############################################
####              Main Menu             ####	
####        1. ip addr show             ####
####        2. ip route                 ####
####        3. ifconfig                 ####
####        4. interfaces               ####
####        5. qosconfig                ####
####        6. _config.php              ####
####        7. Reboot                   ####
####        8. Clear DHCP               ####
############################################
######################R.DiMaggio############
			"""
print(menu)
agsTask = input("Make your selection: ")

print("establishing connection....")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(agsHost, port=22, username=agsU, password=agsP)
print("connection successful..")


if agsTask == "1":
    pmstdin, pmstdout, pmstderr = ssh_client.exec_command("ip addr show")
    output = pmstdout.readlines()
    print(output)
    time.sleep(.5)
    print("Grabbing arp table....")
    time.sleep(.5)
    with open("AGS_ARP.txt", "a") as file:
             file.write('\n'.join(output))
    print("ARP table write finished....")
elif agsTask == "2":
    pmstdin, pmstdout, pmstderr = ssh_client.exec_command("ip route show")
    output = pmstdout.readlines()
    print(output)
    time.sleep(.5)
    input("Done. Hit Enter to continue..")
    time.sleep(.5)
    with open("AGS_Route.txt", "a") as file:
             file.write('\n'.join(output))
    print("IP Route finished....")
elif agsTask == "3":
    pmstdin, pmstdout, pmstderr = ssh_client.exec_command("ifconfig")
    output = pmstdout.readlines()
    time.sleep(.5)
    print("Grabbing Running Config....")
    time.sleep(.5)
    with open("AGS_ifconfig.txt", "a") as file:
             file.write('\n'.join(output))
    print("config grabbed....")
elif agsTask == "4":
    pmstdin, pmstdout, pmstderr = ssh_client.exec_command("more /etc/firewall/interfaces")
    output = pmstdout.readlines()
    time.sleep(.5)
    print("Grabbing Interfaces List....")
    time.sleep(.5)
    with open("AGS_Interfaces.txt", "a") as file:
             file.write('\n'.join(output))
    print("IP ARP list grab successful....")
elif agsTask == "5":#Hangs due to line needing 'more' input
    pmstdin, pmstdout, pmstderr = ssh_client.exec_command("more /etc/firewall/qosconfig.json")
    output = pmstdout.readlines()
    time.sleep(.5)
    print("Grabbing QOS config....")
    time.sleep(.5)
    with open("AGS_qos.txt", "a") as file:
             file.write('\n'.join(output))
    print("Routing Table grab successful....")
elif agsTask == "6":#Hangs due to line needing 'more' input
    pmstdin, pmstdout, pmstderr = ssh_client.exec_command("more /etc/egs/_config.php")
    output = pmstdout.readlines()
    time.sleep(.5)
    print("Grabbing QOS config....")
    print("Grabbing QOS config....")
    time.sleep(.5)
    with open("AGS_qos.txt", "a") as file:
             file.write('\n'.join(output))
    print("Routing Table grab successful....")
elif agsTask == "7":
    pmstdin, pmstdout, pmstderr = ssh_client.exec_command('/bin/su root -c "reboot -fn"', get_pty=True)
    pmstdin.write('PasswordZ\n')
    print("Reboot successful....")
    print("...Returning to main menu")
    time.sleep(1)
#elif agsTask == "8":
#    pmstdin, pmstdout, pmstderr = ssh_client.exec_command('/bin/su root -c "reboot -fn"', get_pty=True)
#    pmstdin.write('clear_leases\n')
#    print("Leases cleared....")
#    time.sleep(10)
else:
    print("..Invalid selection..")
time.sleep(1)