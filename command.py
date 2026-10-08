#Imports
from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess
import os
import psutil
import shutil
import platform 
import socket
#--------------------------------------#

#Conversions
def bytesToGB(bytesToBeConverted):
    return  f'{bytesToBeConverted / (1024**3):.2f}'

#--------------------------------------#

#Command Logic
def exit_program():
    print("Thanks for using local pilot hopefully your laptop isn't bricked :)")
    return False

def clear_shell():
    os.system('cls' if os.name == 'nt' else 'clear') 

def hello():
    return 'Hello there, what do you require today?'

def help():
    return 'CPU: Shows CPU usage, Physical Cores Count and Logical Cores Count. Exit: This is used to exit the program\nDNS: Supples you with the ip address of the host\nHello: This is used to greet the program(Hint: Good way to see if it\'s running!)\nHelp: Shows all available commands.\nPing: Pings supplied Argument\nPort: Checks if port is available\nIpAddr: Displays your Ip Address.\nnetscan: Scans your network for active ips\nRam: Displays total, used and available RAM\nReturnDNS: Is your dns comand reversed. \nStorage: Shows total storage, used storage and Free storage in GB\nSystem: Displays your system details\nTrace: This used to measure the diffrent routers your packet goes tohrough the reach the destenation.'

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

        return True
    else:
        return False 


def dnsLookup(host):
    try:
        dns = socket.gethostbyname(host)
    except socket.gaierror:
        return 'Could not resolve host'

    return dns 

def portCheck(host, port):
        try: 
            port = int(port)
        except ValueError:
            return 'Port must be a number'
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)

        returnCode = s.connect_ex((host, port))

        s.close()

        if returnCode == 0: 
            return True
        else:
            return False

def networkScan():
    ip = ipInfo()
    semiIps = ip.split('.')
    validIps = []

    ips = []

    for lastOctet in range(1, 255): 
            full_ip = f'{semiIps[0]}.{semiIps[1]}.{semiIps[2]}.{lastOctet}'
            ips.append(full_ip)

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(ping, ip): ip for ip in ips}

        completed = 0

        for future in as_completed(futures):
            ip = futures[future]
            result = future.result()

            completed += 1

            print(f'Scanning {completed}/254', end='\r')

            if result:
                validIps.append(ip)

        print()
        return validIps

def trace(host):
    result = subprocess.run(
        ["traceroute", host],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return f'Could not find the trace route to {host}'

    lines = result.stdout.splitlines()

    hops = lines[1:]

    output = [f"Route to {host}:"]

    for hop in hops: 
        output.append(hop.strip())

    return "\n".join(output)

def returnDNS(ip):
    try:
        result =  socket.gethostbyaddr(ip)
        hostname = result[0]

        return f"IP: {ip}\nHostname: {hostname}"

    except socket.herror:
        return f"No hostname found for {ip}"


#--------------------------------------#

#Command Calling
def commandCalling(userCmd):
    #Stores the different commands and arguments
    userCmdList = userCmd.split()
    userCmd = userCmdList[0]

    userCmdArgument1 = None
    userCmdArgument2 = None

    if len(userCmdList) >= 2:
        userCmdArgument1 = userCmdList[1]

    if len(userCmdList) >= 3: 
        userCmdArgument2 = userCmdList[2]


    #Checks if the command exists and calls the function
    if userCmd== 'exit':
        return exit_program()

    elif userCmd == 'clear':
        clear_shell()

    elif userCmd == 'cpu':
        print(cpuInfo())

    elif userCmd == 'dns':
        if userCmdArgument1 is None:
            return 'Please provide another argument for this command'
        else:
            print(dnsLookup(userCmdArgument1))
    
    elif userCmd == 'hello':
        print(hello())

    elif userCmd == 'ipaddr':
        print(ipInfo())

    elif userCmd == 'help':
        print(help())

    elif userCmd == 'netscan':
        print(networkScan())

    elif userCmd == 'ping':
        print(ping(userCmdArgument1))

    elif userCmd == 'port':
        if userCmdArgument1 is None or userCmdArgument2 is None:
            print('Please provide two arguments for this command host & port')
        else:
            print(portCheck(userCmdArgument1, userCmdArgument2))


    elif userCmd == 'ram':
        print(ramInfo())

    elif userCmd == 'reversedns': 
        if userCmdArgument1 is None:
            print('Please provide a arguement for this command')
        else:
            print(returnDNS(userCmdArgument1))

    elif userCmd == 'storage':
        print(storageInfo())

    elif userCmd == 'system':
        print(machineInfo())

    elif userCmd == 'trace':
        if userCmdArgument1 is None:
            print('Please provide a argument for this command')
        else:
            print(trace(userCmdArgument1))

    else:
        print('Command not recognised :(')

    return True
#--------------------------------------#
