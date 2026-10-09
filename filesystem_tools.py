from pathlib import Path 

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
 