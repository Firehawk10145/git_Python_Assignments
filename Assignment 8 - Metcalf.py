import os
curDir = os.getcwd()
print(curDir)

def fileCreator():
    name = input(str("Please input your name. "))
    address = input(str("Please input your address. "))
    phoneNumber = input("Please input your phone number. (No dashes) ")
    comma = ','
    with open(completePath,'w') as fileHandle:
        fileHandle.write(name)
        fileHandle.write(comma)
        fileHandle.write(address)
        fileHandle.write(comma)
        fileHandle.write(phoneNumber)
    with open(completePath,'r') as fileHandle:
        data = fileHandle.read
        print(data)

         
dirPrompt=True
while dirPrompt:
    filePath = input("\nPlease input the directory you would like to store your file in. ")
    if os.path.exists(filePath):
        print("\nDirectory exists")
    else:
        print("\nDirectory does not exists")
    print('\nDo you want to look up another path? (yes or no)')
    tryAgain = input(str())
    if tryAgain not in ("yes","y"):
        break
fileName = 'testFile.txt'
completePath = filePath + fileName   
fileCreator()
            