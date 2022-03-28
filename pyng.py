# Pyng
# Find other devices on local network using MacOS
import os

# Global Variables
info = 'info.txt'
ip_info = f'ifconfig | cat > {info}'
ping_count = 1
ping_result = 'ping_result.txt'

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

subnet = ip.split('.')

var = open(ping_result, "w")
var.write(ip)
var.close()

def speedy(subnet, ping_result):
	if subnet[0] == '10':
		for host in range(1, 255):
			if not host == subnet[3]:
				a = f'{subnet[0]}.0.0.{host}'
				command = f'ping {a} -c 1 -W .3 | cat >> {ping_result}'
				os.system(command)
	elif subnet[0] == '172' and subnet[1] < '32' and subnet[1] >= '16':
		for host in range(1, 255):
			if not host == subnet[3]:
				a = f'{subnet[0]}.0.0.{host}'
				command = f'ping {a} -c 1 -W .3 | cat >> {ping_result}'
				os.system(command)
	elif subnet[0] == '192' and subnet[1] == '168':
		for host in range(1,255):
			if not host == subnet[3]:
				a = f'{subnet[0]}.0.0.{host}'
				command = f'ping {a} -c 1 -W .3 | cat >> {ping_result}'
				os.system(command)
	else:
		print('Error: IP Address outside supported range')

def verbose(subnet, ping_count, ping_result):
	if subnet[0] == '10': # class A IP Address
		for n in range(0, 256):
			for net in range(0, 256):
				for host in range(1,255):
					if not host == subnet[3]:
						a = f'{subnet[0]}.{n}.{net}.{host}'
						command = f'ping {a} -c {ping_count} | cat >> {ping_result}'
						os.system(command)
	elif subnet[0] == '172' and subnet[1] < '32' and subnet[1] >= '16': # class B IP Address
		for n in range(16, 32):
			for net in range(0, 256):
				for host in range(1,255):
                			if not host == subnet[3]:
                        			a = f'{subnet[0]}.{n}.{net}.{host}'
                        			command = f'ping {a} -c {ping_count} | cat >> {ping_result}'
                        			os.system(command)
	elif subnet[0] == '192' and subnet[1] == '168': # class C IP Address
		for net in range(0, 256):
			for host in range(1,255):
                		if not host == subnet[3]:
                        		a = f'{subnet[0]}.{subnet[1]}.{net}.{host}'
                        		command = f'ping {a} -c {ping_count} | cat >> {ping_result}'
                        		os.system(command)
	else:
		print('Error: IP Address outside supported range')

speedy(subnet, ping_result)
