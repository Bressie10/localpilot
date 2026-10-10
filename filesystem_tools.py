from pathlib import Path 
import os

def pwdFunc():
    return Path.cwd()

#This took way too long for some reason just don't touch it pretty please  
def lsFunc(hidden = None):
    path = pwdFunc()
    result = list(path.iterdir())
    fileOutput = []

    #Loops through the list of items and gets the name of the last section of the file path
    for item in result:
        lastFile = item.name

        #Checks if user wants to see hidden files and skips the iteration if not wanted
        if hidden is None and lastFile[0] == '.':
                        continue

        elif hidden == '-a' or hidden is None:
            #Checks if item is a directory or file
            if item.is_dir():
                fileOutput.append(f'[Dir]: {lastFile}')
            elif item.is_file():
                fileOutput.append(f'[File]: {lastFile}')

        else:
            return 'Command not recognised :('
        
    #checks if pwd is empty
    if len(fileOutput) >= 1:
        strFileOutput = '\n'.join(fileOutput)
        return f'{strFileOutput}\n\nThere is {len(fileOutput)} item(s) in this directory'
    
    return 'There are no items in this directory'

#Believe it or not everything ran in this function first try, Top 1 so far
def cdFunc(target_dir):
    if target_dir == '~':
        home = Path.home()
        os.chdir(home)
        return 'You are home'

    #Converts it into a path
    target_dir = Path(target_dir)

    if target_dir.is_absolute(): 
        fullPath = target_dir

    else:
        initialPath = pwdFunc()
        fullPath = initialPath / target_dir


    try:
        os.chdir(fullPath)
    except FileNotFoundError:
        return "This folder doesn't exist."

    except NotADirectoryError:
        return 'This is not a directory'

    return f'You are in {pwdFunc()}'

def mkdirFunc(target_dir):

    target_dir = Path(target_dir)
    
    if target_dir.is_absolute(): 
            fullPath = target_dir
    
    else:
        initialPath = pwdFunc()
        fullPath = initialPath / target_dir

    try:
        fullPath.mkdir()
        return "Folder created!(I'm surprised it works tbh)"

    except FileExistsError:
        return 'Folder already exists'

def touchFunc(targetFile):
    targetFile = Path(targetFile)
         
    if targetFile.is_absolute(): 
        fullPath = targetFile
         
    else:
        initialPath = pwdFunc()
        fullPath = initialPath / targetFile

    fileName = fullPath.name 

    try:
        fullPath.touch(exist_ok=False)  
        return f'Success: {fileName} was created'
    except:
        return 'This file already exists'