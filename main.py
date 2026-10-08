import platform
import socket

#Gathers machine info
def machineInfo():
    operatingSystem = platform.system()
    hostname = socket.gethostname()
    processorArchitecture = platform.machine()
    return f'{operatingSystem}\n{hostname}\n{processorArchitecture}'

#CLI Output
print('Hello there....\nWelcome to local pilot\nHow can I help you today')
programRunning = True

#Takes user input
while programRunning:
    userCmd = input('Please enter your command: ')
    userCmd = userCmd.lower().strip()

    #Checks if user wants to exit
    if userCmd == 'exit':
            programRunning = False
            print("Thanks for using local pilot hopefully your laptop isn't bricked :)")

    print(f'You ran the command {userCmd}')

    #Command Logic
    if userCmd == 'hello':
        print('Hello there, what do you require today?')

    elif userCmd == 'help':
        print('1.Exit: This is used to exit the program\n2.Hello: This is used to greet the program(Hint: Good way to see if it\'s running!)\n3.Help: Shows all available commands.\n4.System: Displays your system details') 

    elif userCmd == 'system':
         print(machineInfo())
