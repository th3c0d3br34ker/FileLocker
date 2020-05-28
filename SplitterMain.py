from os import chdir, listdir
from traceback import print_exc
from EssentialsCore import cleanit, getInput
from EssentialsCore import default_dir, locked_folder_path, testfiles_folder_path, output_files_folder


def start():
    system("cls")
    print("\n **************************************** WELCOME **************************************** \n")
    print(" Press 1 to Hide. \n Press 2 to Recover. \n Press 3 to Exit.")
    option = getInput(inpstring="\n Enter Choice : ",
                      datatype=int, options=[x for x in range(1, 5)])
    if(option == 1):
        randomize()
        print("\n Thank You!")
    elif(option == 2):
        derandomize()
        print("\n Thank You!")
    elif(option == 3):
        print("\n Exiting...")
        exit()
    else:
        print("\n Invalid Choice!")
        exit()


def randomize():
    try:
        # Import relevant Modules.
        from os.path import isfile
        from fileLockCore import randomizer

        print("\nLooking for files in local directory...\n")
        chdir(testfiles_folder_path)
        print("Currently in : {}\n".format(testfiles_folder_path))
        filelist = [x for x in listdir(testfiles_folder_path) if isfile(x)]
        n = len(filelist)
        print("List of Files :")
        for i in range(n):
            print("{0}. {1} ".format(i+1, filelist[i]))

        # Getting the file from the user.
        filename = filelist[getInput(inpstring="\nEnter file number : ", datatype=int, options=[
                                     x for x in range(1, n+1)])-1]

        # Sending the file to the Program.
        randomizer(filename)
        chdir(default_dir)
    except Exception:
        print_exc()


def derandomize():
    try:
        # Import relevant Modules.
        from fileLockCore import derandomizer

        print("\nLooking for files in local directory...\n")
        #print("Only works with TestFiles Directory")
        chdir(locked_folder_path)
        print("Currently in : {}\n".format(locked_folder_path))
        folderlist = [x for x in listdir(locked_folder_path)]
        n = len(folderlist)
        option = [x for x in range(1, n+1)]
        print("List of Folders :")

        for i in range(n):
            print("{0}. {1} ".format(i+1, folderlist[i]))
        # Getting the folder from the user.
        foldername = folderlist[getInput(
            inpstring="\nEnter folder number : ", datatype=int, options=option)-1]

        # Sending the file to the Program.
        derandomizer(foldername)
        chdir(default_dir)
    except Exception:
        print_exc()


def displayInfo():
    from os.path import exists
    print("Files Directory : {} ...{}".format(
        testfiles_folder_path, exists(testfiles_folder_path)))
    print("Output Directory : {} ... {}".format(
        output_files_folder, exists(testfiles_folder_path)))
    print("Default Directory : {} ... {}".format(
        default_dir, exists(testfiles_folder_path)))


if __name__ == '__main__':
    displayInfo()
    start()
