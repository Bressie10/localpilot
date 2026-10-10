#Imports
from command import commandCalling

#CLI Output
print('Hello there....\nWelcome to local pilot\nHow can I help you today')
programRunning = True

#Takes user input
while programRunning:
    userCmd = input('Please enter your command: ')
    userCmd = userCmd.lower().strip()

    programRunning = commandCalling(userCmd)


