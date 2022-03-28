import pythonping, os

# Global Variables
info = 'info.txt'
ip_info = f'ifconfig | cat > {info}'

# Commands
os.system(ip_info)



