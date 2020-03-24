from traceback import print_exc
from os import getcwd


default_dir = "D:\\Jainam Desai\\Documents\\Projects\\FileSecurity"
locked_folder_path = default_dir+"\\Locked\\"
testfiles_folder_path = default_dir+"\\TestFiles\\"
output_files_folder = default_dir+"\\Output\\"


def digitBlancer(n, size = 6):
    s = '0' * (size-len(str(n)))
    return s+str(n)

def randomGenerate(n):
    try:
        from random import sample

        size = len(str(n))+1
        count_list = sample(range(0, n), n)
        random_count_list = list(map(lambda x : digitBlancer(x, size), count_list))
        return random_count_list
    except Exception:
        print_exc()

def randomSizeGenerate(size):
    try:
        from random import randint

        size_list = []
        exp = 0.5
        while(size>0):
            tmp = randint(1, int(size**exp))
            size_list.append(tmp)
            size = size - tmp
        return size_list
    except Exception:
        print_exc()

def cleanit():
    try:
        from os import listdir, remove, system
        from os.path import isdir

        print("\nCleaning Test files Folder:", testfiles_folder_path)
        files = listdir(testfiles_folder_path)

        for f in files:
            if isdir(f) and '_partfiles' in f:
                print("Cleaing {}".format(f))
                remove(locked_folder_path + f)
        
        print("\nCleaned.")

        print("\nCleaning Locked Folder:", locked_folder_path)
        files = listdir(locked_folder_path)

        for f in files:
            print("Cleaing {}".format(f))
            remove(locked_folder_path + f)
        
        print("\nCleaned.")

        print("\nCleaning Output Folder:", output_files_folder)
        files = listdir(output_files_folder)

        for f in files:
            print("Cleaing {}".format(f))
            remove(output_files_folder + f)
        
        print("\nCleaned.")
        
    except Exception:
        print_exc()

def getInput(inpstring='', datatype=None, options=[]):
    if datatype == int:
        options=list(map(str, options))
        print(inpstring, end='')
        inp = input()
        isnum = inp.isdigit()
        inoptions = inp in options
        while (not isnum or not inoptions):
            print(" Invalid Input!")
            if(not isnum):
                print(" Enter a Number")
            if(not inoptions):
                print(" Enter a Number in range:","\n " ," ".join(options))
            print(inpstring, end='')
            inp = input()
            isnum = inp.isdigit()
            inoptions = inp in options
        return int(inp)
    
    if datatype == str:
        print(inpstring, end='')
        inp = input()
        return inp

    if datatype == 'file':
        from os.path import isfile
        print(inpstring, end='')
        inp = input()
        inpF = output_files_folder+inp
        isFile = isfile(inpF)
        while(not isFile):
            print(isFile)
            print(inpstring, end='')
            inp = input()
            inpF = output_files_folder+inp
            isFile = isfile(inpF)
        
        return inpF       
        
    if datatype == None:
        print("\n Input datatype not specified!")
        return None

def getHash(logF):
    # Import relevant modules.
    from hashlib import sha256
    data = "".encode()
    with open(logF,'rb') as file:
        data = file.read()
    return sha256(data).hexdigest()
