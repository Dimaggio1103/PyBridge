import re

header = "Speadsheet | PanelPort |    IP Address  | Switch Port "
file = "MarquiPorts.txt"
infile = open(file, 'r')
lines = infile.readlines()
lines[0:10]

portMatrix = input("What panel port is it? Format = '005-B' \n").upper()
for line in lines:
	if re.search(portMatrix, line):
		print(header)
		print(line)