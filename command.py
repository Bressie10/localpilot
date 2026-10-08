#Imports

import platform 
import socket
#--------------------------------------#

#Command Logic
def exit_program():
    print("Thanks for using local pilot hopefully your laptop isn't bricked :)")
    return False 

def hello():
    return 'Hello there, what do you require today?'

def help():
    return '1.Exit: This is used to exit the program\n2.Hello: This is used to greet the program(Hint: Good way to see if it\'s running!)\n3.Help: Shows all available commands.\n4.System: Displays your system details'

def machineInfo():
    operatingSystem = platform.system()
    hostname = socket.gethostname()
    processorArchitecture = platform.machine()
    return f'{operatingSystem}\n{hostname}\n{processorArchitecture}'


#--------------------------------------#

#Command Calling
def commandCalling(userCmd):
    if userCmd == 'exit':
        return exit_program()
            
    elif userCmd == 'hello':
        print(hello())

    elif userCmd == 'help':
        print(help())

    elif userCmd == 'system':
        print(machineInfo())

    else:
        print('Command not recognised :(')

    return True
#--------------------------------------#
