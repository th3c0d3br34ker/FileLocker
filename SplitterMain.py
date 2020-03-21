from os import chdir, getcwd, listdir, path, system, remove
from fileSplitCore import randomizer, derandomizer
from EssentialsCore import cleanit
from EssentialsCore import testfiles_folder_path, default_dir, locked_folder_path

def main():
    print("\n******************************  Welcome  *****************************\n")
    print("Enter 1 to Hide\nEnter 2 to Recover")
    option = int(input())
    if(option == 1):
        randomize()
    elif(option == 2):
        derandomize()
    elif(option == 3):
        cleanit()
        system('cls')
    else:
        print("Invalid choice")
        system('cls')
        main()
    
    print("\nThank You!")


def randomize():
    print("\nLooking for files in local directory...\n")
    #print("Only works with TestFiles Directory")
    chdir(testfiles_folder_path)
    print("Currently in : {}\n".format(testfiles_folder_path))
    filelist = [x for x in listdir(testfiles_folder_path) if path.isfile(x)]
    n = len(filelist)
    print("List of Files :")
    for i in range(n):
        print("{0}. {1} ".format(i+1, filelist[i]))
    
    #Getting the file from the user.
    print("\nEnter file number : ", end='')
    filename = filelist[int(input())-1]
    
    #Sending the file to the Program.
    randomizer(filename)
    chdir(default_dir)   
    

def derandomize():
    print("\nLooking for files in local directory...\n")
    #print("Only works with TestFiles Directory")
    chdir(locked_folder_path)
    print("Currently in : {}\n".format(locked_folder_path))
    filelist = [x for x in listdir(locked_folder_path)]
    n = len(filelist)
    print("List of Folders :")
    for i in range(n):
        print("{0}. {1} ".format(i+1, filelist[i]))
    #Getting the folder from the user.
    print("\nEnter folder number : ", end='')
    foldername = filelist[int(input())-1]
    
    #Sending the file to the Program.
    derandomizer(foldername)
    chdir(default_dir)


if __name__ == '__main__':
    system("cls")
    main()
    