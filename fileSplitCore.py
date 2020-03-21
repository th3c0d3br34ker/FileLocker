from os import getcwd, chdir, path, remove
from traceback import print_exc

# It splits a fils, stores the correct order in a log a file.
# Then joins the file just in order
def randomizer(filename):
    try:
        #Import Specific Modules.
        from fileSplitRandomizerCore import zipFileMaker, fileSplitter
        from KeyManager import keyEncryptor
        from EssentialsCore import output_files_folder
        file_size = path.getsize(filename)
        foldername, keyData = fileSplitter(filename, file_size)
        zipFileMaker(foldername)
        print("\nEnter KeyFile name : ",end='')
        key = input()
        keyEncryptor(keyData, keyFile=output_files_folder+key)
    except:
        print_exc()
        

# It splits a file there itself.
# Then it joins the file in correct file from the log file.
def derandomizer(foldername):
    try:
        #Import Specific Modules.
        from fileSplitDerandomizerCore import unZipper, fileJoiner
        from KeyManager import keyDecryptor
        from EssentialsCore import output_files_folder
        print("\nEnter KeyFile name : ",end='')
        key = input()
        keyData = keyDecryptor(output_files_folder+key)
        if keyData.split('\n')[0] == foldername.split('.')[0]: 
            print("\nKey Matched!")
            foldername = unZipper(foldername)
            keyData = keyData.split('\n')
            logF = output_files_folder+foldername+'\\'+keyData[1]
            fileJoiner(foldername,log=logF,ext=keyData[2])
            
            # Delete Key
            print("\nKey Deleted.")
            remove(output_files_folder+key)
        else:
            print("\nKey did not Match!")    
    except:
        print_exc()
     