# Pyng
# Find other devices on local network using MacOS
import pythonping, os

# Global Variables
info = 'info.txt'
ip_info = f'ifconfig | cat > {info}'

# Commands
os.system(ip_info)

# Read in network info from ip config file
temp = open(info)
networks = temp.readlines()
temp.close()

count = 0
for item in networks:
	count += 1
	if item[:4] == 'en0:':
		break

network = networks[count+3]
address = network.split(" ")
ip = address[1]
print(ip)

subnets = ip.split('.')
for net in subnets:
	print(net)


