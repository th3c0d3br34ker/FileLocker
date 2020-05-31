from os import getcwd, chdir, remove
from os.path import getsize, exists
from traceback import print_exc
from core.EssentialsCore import getInput

# It splits a fils, stores the correct order in a log a file.
# Then joins the file just in order


def randomizer(filename):
    try:
        # Import Specific Modules.
        from core.fileSplitLockerCore import zipFileMaker, fileSplitter
        from core.KeyManager import keyEncryptor
        from core.EssentialsCore import output_files_folder

        file_size = filename.stat().st_size
        foldername, keyData = fileSplitter(filename, file_size)
        zipFileMaker(foldername)
        key = getInput(inpstring="\nEnter KeyFile name : ", datatype=str)
        keyEncryptor(keyData, keyFile=output_files_folder.joinpath(key))
    except:
        print_exc()

# It splits a file there itself.
# Then it joins the file in correct file from the log file.


def derandomizer(foldername):
    try:
        # Import Specific Modules.
        from core.fileSplitUnlockerCore import unZipper, fileJoiner, matchKey
        from core.KeyManager import keyDecryptor
        from core.EssentialsCore import output_files_folder

        # Get Key file.
        key = getInput(inpstring="\nEnter KeyFile name : ", datatype='file')
        keyData = keyDecryptor(key).split('\n')
        if matchKey(keyData[3], keyData[2], foldername):
            print("\n Key Matched!")
            foldername = unZipper(foldername)
            logF = foldername.joinpath(keyData[2])
            fileJoiner(foldername, log=logF, fname=keyData[0], ext=keyData[1])

            # Delete Key
            print("\n Key Deleted.")
            remove(key)
        else:
            print("\n Key did not Match!")
    except FileNotFoundError:
        print("\n Unable to read KEY.")
    except:
        print_exc()
