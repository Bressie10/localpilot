#Import Libaries
import psutil 
import shutil
import platform
import socket

#-----------------------#


#Converts Bytes to GBs 
def bytesToGB(bytesToBeConverted):
    return  f'{bytesToBeConverted / (1024**3):.2f}'

def machineInfo():
    operatingSystem = platform.system()
    hostname = socket.gethostname()
    processorArchitecture = platform.machine()
    return f'{operatingSystem}\n{hostname}\n{processorArchitecture}'

#Gets storage Info 
def storageInfo():
    total, used, free = shutil.disk_usage("/")

    #Converts from bytes - GB
    return f'Total Disk Space: {bytesToGB(total)}GB\nUsed Disk Space: {bytesToGB(used)}GB\nFree Disk Space: {bytesToGB(free)}GB'

#Gets Ram Info 
def ramInfo():
    ram = psutil.virtual_memory()

    return f'Total RAM: {bytesToGB(ram.total)}GB\nUsed RAM: {bytesToGB(ram.used)}GB\nAvailable Ram: {bytesToGB(ram.available)}GB'

#I say you can take a good guess :)
def cpuInfo():
    cpu = psutil

    return f'CPU Usage: {cpu.cpu_percent()}%\nPhysical Cores: {cpu.cpu_count(logical=False)}\nLogical Cores: {cpu.cpu_count(logical=True)}'

#Blows up laptop or gets your ip one of the two.....
def ipInfo(): 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))

    ipAddress = s.getsockname()[0]

    s.close() 

    return ipAddress
