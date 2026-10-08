#Imports
import subprocess
import os
import psutil
import shutil
import platform 
import socket
#--------------------------------------#
def bytesToGB(bytesToBeConverted):
    return  f'{bytesToBeConverted / (1024**3):.2f}'


#Command Logic
def exit_program():
    print("Thanks for using local pilot hopefully your laptop isn't bricked :)")
    return False

def clear_shell():
    os.system('cls' if os.name == 'nt' else 'clear') 

def hello():
    return 'Hello there, what do you require today?'

def help():
    return 'CPU: Shows CPU usage, Physical Cores Count and Logical Cores Count. Exit: This is used to exit the program\nDNS: Supples you with the ip address of the host\nHello: This is used to greet the program(Hint: Good way to see if it\'s running!)\nHelp: Shows all available commands.\nPing: Pings supplied Argument\nIpAddr: Displays your Ip Address.\nRam: Displays total, used and available RAM\nStorage: Shows total storage, used storage and Free storage in GB\nSystem: Displays your system details'

def machineInfo():
    operatingSystem = platform.system()
    hostname = socket.gethostname()
    processorArchitecture = platform.machine()
    return f'{operatingSystem}\n{hostname}\n{processorArchitecture}'

def storageInfo():
    total, used, free = shutil.disk_usage("/")

    #Converts from bytes - GB
    return f'Total Disk Space: {bytesToGB(total)}GB\nUsed Disk Space: {bytesToGB(used)}GB\nFree Disk Space: {bytesToGB(free)}GB'

def ramInfo():
    ram = psutil.virtual_memory()

    return f'Total RAM: {bytesToGB(ram.total)}GB\nUsed RAM: {bytesToGB(ram.used)}GB\nAvailable Ram: {bytesToGB(ram.available)}GB'

def cpuInfo():
    cpu = psutil

    return f'CPU Usage: {cpu.cpu_percent()}%\nPhysical Cores: {cpu.cpu_count(logical=False)}\nLogical Cores: {cpu.cpu_count(logical=True)}'

def ipInfo(): 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))

    ip_address = s.getsockname()[0]

    s.close()

    return ip_address

def ping(host):
    result = subprocess.run(
        ['ping', '-c', '1', host],
        capture_output=True,
        text=True 
    )

    if result.returncode == 0:
        time_value = result.stdout.split("time=")[1].split()[0]
        return f"Host '{host}' can be reached\nTime: {time_value}"
    else:
        return f"Host '{host}' cannot be reached"


def dnsLookup(host):
    try:
        dns = socket.gethostbyname(host)
    except socket.gaierror:
        return 'Could not resolve host'

    return dns 


#--------------------------------------#

#Command Calling
def commandCalling(userCmd):
    userCmdList = userCmd.split()
    userCmd = userCmdList[0]
    if len(userCmdList) > 1:
        userCmdArguments = userCmdList[1]
    else:
        userCmdArguments = None


    if userCmd== 'exit':
        return exit_program()

    elif userCmd == 'clear':
        clear_shell()

    elif userCmd == 'cpu':
        print(cpuInfo())

    elif userCmd == 'dns':
        print(dnsLookup(userCmdArguments))
    
    elif userCmd == 'hello':
        print(hello())

    elif userCmd == 'ipaddr':
        print(ipInfo())

    elif userCmd == 'help':
        print(help())

    elif userCmd == 'ping':
        print(ping(userCmdArguments))

    elif userCmd == 'ram':
        print(ramInfo())

    elif userCmd == 'storage':
        print(storageInfo())

    elif userCmd == 'system':
        print(machineInfo())

    else:
        print('Command not recognised :(')

    return True
#--------------------------------------#
