#Imports
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

def hello():
    return 'Hello there, what do you require today?'

def help():
    return 'CPU: Shows CPU usage, Physical Cores Count and Logical Cores Count. Exit: This is used to exit the program\nHello: This is used to greet the program(Hint: Good way to see if it\'s running!)\nHelp: Shows all available commands.\nRam: Displays total, used and available RAM\nStorage: Shows total storage, used storage and Free storage in GB\nSystem: Displays your system details'

def machineInfo():
    operatingSystem = platform.system()
    hostname = socket.gethostname()
    processorArchitecture = platform.machine()
    return f'{operatingSystem}\n{hostname}\n{processorArchitecture}'

def storageInfo():
    total, used, free = shutil.disk_usage("/")

    #Converts from bytes - GB
    gb = 1024 ** 3
    return f'Total Disk Space: {bytesToGB(total)}GB\nUsed Disk Space: {bytesToGB(used)}GB\nFree Disk Space: {bytesToGB(free)}GB'

def ramInfo():
    ram = psutil.virtual_memory()

    return f'Total RAM: {bytesToGB(ram.total)}GB\nUsed RAM: {bytesToGB(ram.used)}GB\nAvailable Ram: {bytesToGB(ram.available)}GB'

def cpuInfo():
    cpu = psutil

    return f'CPU Usage: {cpu.cpu_percent()}%\nPhysical Cores: {cpu.cpu_count(logical=False)}\nLogical Cores: {cpu.cpu_count(logical=True)
}'

#--------------------------------------#

#Command Calling
def commandCalling(userCmd):
    if userCmd == 'exit':
        return exit_program()

    elif userCmd == 'cpu':
        print(cpuInfo())
            
    elif userCmd == 'hello':
        print(hello())

    elif userCmd == 'help':
        print(help())

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
