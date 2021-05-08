import os, sys
import requests
from datetime import datetime

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(os.path.basename(fullPath))
                
    return allFiles



def checkServer(file, deleted_file_name):
    print(f"Checking file: {file}...")
    url = "https://i.vsco.co/"
    r = requests.get(url + os.path.splitext(file)[0]) #Eliminate file extension from file name
    if r.status_code == 404:
        print(f"File {file} not found.")
        with open(deleted_file_name, 'a') as deleted:
            deleted.write(file + "\n")




if __name__ == "__main__":
    deleted_file_name = "deleted" + datetime.now().strftime("%d-%m-%Y__%H%M%S" + ".txt")
    dirName = sys.argv[1]
    fileList = getListOfFiles(dirName)
    for file in fileList:
        checkServer(file, deleted_file_name)
