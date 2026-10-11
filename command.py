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

from filesystem_tools import (
    pwdFunc,
    lsFunc,
    cdFunc,
    mkdirFunc,
    touchFunc,
    rmFunction,
    mvFunction,
    cpFunc,
    catFunc,
    findFunc
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
    return '''
    CPU: Shows CPU usage, Physical Cores Count and Logical Cores Count. Exit: This is used to exit the program\n
    DNS: Supples you with the ip address of the host\nHello: This is used to greet the program(Hint: Good way to see if it\'s running!)\n
    Help: Shows all available commands.\nPing: Pings supplied Argument\nPort: Checks if port is available\n
    PWD: Returns your current working directory\n
    IpAddr: Displays your Ip Address.\nnetscan: Scans your network for active ips\n
    Ram: Displays total, used and available RAM\nReturnDNS: Is your dns comand reversed.\n
    Storage: Shows total storage, used storage and Free storage in GB\nSystem: Displays your system details\n
    Trace: This used to measure the diffrent routers your packet goes tohrough the reach the destenation.
    Ls: Lists all files and directories in your pwd\n
    cd: To navigate to different directories in your pwd\n
    mkdir: Makes a direcotry in your pwd with the name provided\n
    touch: Creates a file in your pwd\n 
    rm: Deletes a file in your pwd\n
    mv: Moves a file or directory to specified location or renames file\n
    cp: Copies a file or directory to specified location or renames file\n
    cat: Returns data in file\n 
    find: Finds a file name recursively from your pwd\n
    '''

#--------------------------------------#
#Improved logic for identifiying commands
#TO DO
#Make it accept commands with arguments
commands = {
        'netscan' : (networkScan, 0),
        'help' : (help, 0),
        'hello' : (hello, 0),
        'cpu' : (cpuInfo, 0), 
        'ram' : (ramInfo, 0), 
        'storage' : (storageInfo, 0),
        'system' : (machineInfo, 0),
        'ipaddr' : (ipInfo, 0),
        'dns'  : (dnsLookup, 1),
        'port' : (portCheck, 2),
        'ping' : (ping, 1),
        'reverse_dns' : (returnDNS, 1),
        'trace' : (trace, 1),
        'pwd' : (pwdFunc, 0),
        'ls' : (lsFunc, 1.5),
        'cd' : (cdFunc, 1),
        'mkdir' : (mkdirFunc, 1),
        'touch' : (touchFunc, 1),
        'rm' : (rmFunction, 1),
        'mv' : (mvFunction, 2),
        'cp': (cpFunc, 2),
        'cat' : (catFunc, 1),
        'find' : (findFunc, 1)
    }
#--------------------------------------#

#Command Calling
def commandCalling(userCmd):
    #Stores the different commands and arguments
    userCmdList = userCmd.split()
    if not userCmdList:
        return True
    userCmd = userCmdList[0]

    userCmdArgument1 = None
    userCmdArgument2 = None

    if len(userCmdList) >= 2:
        userCmdArgument1 = userCmdList[1]

    if len(userCmdList) >= 3: 
        userCmdArgument2 = userCmdList[2]

#---------------------------------------#

    #Checks if the command exists and calls the function
    if userCmd in commands:
        if commands[userCmd][1] == 0:
            print(commands[userCmd][0]())

        if commands[userCmd][1] == 1:
            if userCmdArgument1 is None:
                        print('Please provide a arguement for this command')
            else:
                print(commands[userCmd][0](userCmdArgument1))

        if commands[userCmd][1] == 1.5:
            if userCmdArgument1 == None:
                print(commands[userCmd][0]())
            
            else:
                print(commands[userCmd][0](userCmdArgument1))

        if commands[userCmd][1] == 2:
            if userCmdArgument1 is None or userCmdArgument2 is None:
                print('Please provide two arguments for this command')
            else:
                print(commands[userCmd][0](userCmdArgument1, userCmdArgument2))
    elif userCmd == 'exit':
            return exit_program()

    elif userCmd == 'clear':
        clear_shell()


    else:
        print('Command not recognised :(')

    #DO NOT DELETE KEEPS MAIN PROGAM RUNNING, LAPTOP WILL BRICK!!!!!!!!!(It won't rlly I just keep deleting this by accident)
    return True 

#Updated command calling function for web hosting  

def commandCallingWeb(userCmd):
    userCmdList = userCmd.split()

    if not userCmdList:
         return ""

    userCmd = userCmdList[0]

    userCmdArgument1 = None
    userCmdArgument2 = None

    if len(userCmdList) >= 2:
        userCmdArgument1 = userCmdList[1]

    if len(userCmdList) >= 3:
         userCmdArgument2 = userCmdList[2]

    if userCmd in commands:
        argCount = commands[userCmd][1]
        commandFunc = commands[userCmd][0]

        if argCount == 0:
           return commandFunc()

        if argCount == 1:
            if userCmdArgument1 is None:
                return "Please provide an argument for this command"
            return commandFunc(userCmdArgument1)

        if argCount == 1.5:
            if userCmdArgument1 is None:
                return commandFunc()
            return commandFunc(userCmdArgument1)

        if argCount == 2:
            if userCmdArgument1 is None or userCmdArgument2 is None:
                return "Please provide two arguments for this command"
            return commandFunc(userCmdArgument1, userCmdArgument2)

    elif userCmd == "exit":
        return "Exit is disabled in the web demo"

    elif userCmd == "clear": 
        return ""

    return "Command not recognised :("


    