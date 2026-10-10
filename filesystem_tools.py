from pathlib import Path 
import os
import subprocess

def pwdFunc():
    result = subprocess.run(
        ["./native/pwd"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def pathCleaning(target_item):
    target_item = Path(target_item)
         
    if target_item.is_absolute(): 
        fullPath = target_item
         
    else:
        initialPath = pwdFunc()
        fullPath = initialPath / target_item

    return fullPath

     
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

    fullPath = pathCleaning(target_dir)

    try:
        os.chdir(fullPath)
    except FileNotFoundError:
        return "This folder doesn't exist."

    except NotADirectoryError:
        return 'This is not a directory'

    return f'You are in {pwdFunc()}'

def mkdirFunc(target_dir):

    fullPath = pathCleaning(target_dir)

    try:
        fullPath.mkdir()
        return "Folder created!(I'm surprised it works tbh)"

    except FileExistsError:
        return 'Folder already exists'

def touchFunc(targetFile):
    fullPath = pathCleaning(targetFile)

    fileName = fullPath.name 

    try:
        fullPath.touch(exist_ok=False)  
        return f'Success: {fileName} was created'
    except FileExistsError:
        return 'This file already exists'

def rmFunction(targeted_file):
    fullPath = pathCleaning(targeted_file)
    fileName = fullPath.name

    try:
        fullPath.unlink()

    except FileNotFoundError:
        return f'Could not find {fileName}'

    except IsADirectoryError:
        return f'{fileName} is a directory'

    return f'{fileName} was deleted'

def mvFunction(source, destination):
    current_location = pathCleaning(source)
    future_location = pathCleaning(destination)

    destinationFileName = future_location.name

    if not current_location.exists():
        return 'Cannot find specified file' 

    if not future_location.exists():
        current_location.rename(future_location)
        return f'File moved/renamed to {destinationFileName}'

    try:
        new_location = current_location.move_into(future_location)

    except NotADirectoryError: 
        return 'Location specified is not a directory'
    return f'File moved to {new_location}'

def cpFunc(source, destination):
    source_location = pathCleaning(source)
    destination_location = pathCleaning(destination) 
    destination_location_file = destination_location / source_location.name

    if not source_location.exists():
        return 'Could not find source location'

    if not destination_location.is_dir():
        return 'Destination is not a directory'

    if destination_location_file.exists():
        permission = input(f'Do you wish to overwrite {destination_location_file} y/n: ')
        permission = permission.lower()
        if permission == 'n':
            return 'Permission denied'
        elif permission != 'y':
            return 'Please enter a valid command'


    copyLocation = source_location.copy_into(destination_location)

    return f'File copied to {copyLocation}'

def catFunc(source):
    sourcePath = pathCleaning(source)

    try:
        fileContent = sourcePath.read_text(encoding=None, errors=None, newline= None)
        return fileContent
    except FileNotFoundError:
        return f'Could not find {sourcePath.name}'
    except IsADirectoryError as e:
        return f'Cannot read directory: {e}'

def findFunc(pattern):
    pattern = f"'*{pattern}*'"
    startingDirPath = pwdFunc()
    results = list(startingDirPath.rglob(pattern))
    if len(results) == 0:
        return f'No files found'
    
    results = '\n'.join(str(item) for item in results)
    return f'These patterns were found:\n{results}'