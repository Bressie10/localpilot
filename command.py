#Imported functions
#From system tools file
from system_tools import (
    machineInfo,
    storageInfo,
    cpuInfo,
    ramInfo,
    ipInfo
)

from networking_tools import (
    ping,
    dnsLookup,
    portCheck,
    networkScan,
    trace,
    returnDNS
)

#Imported Libarires
import os

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
