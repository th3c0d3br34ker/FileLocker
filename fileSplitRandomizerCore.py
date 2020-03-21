from tqdm import tqdm
from os import chdir, getcwd, listdir, path, remove, mkdir, rmdir
from zipfile import ZipFile,ZIP_STORED
from traceback import print_exc
from EssentialsCore import digitBlancer, randomGenerate, randomSizeGenerate
from EssentialsCore import locked_folder_path, testfiles_folder_path


# It creates a new directory and splits a file there
# genertes a logfile
# returns the foldername
def fileSplitter(filename, size):    
    try:
        key = []
        logF = ""
        foldername = filename+"_partfiles"
        chunk_size_list = randomSizeGenerate(size)
        random_count_list = randomGenerate(len(chunk_size_list)+1)

        print("\n{} will be splitted into {} parts.".format(filename, len(chunk_size_list)))

        # Strart Splitting the file.
        with open(filename,'rb') as main_file:
            logF = random_count_list.pop()

            # Make the directory
            mkdir(foldername)
            chdir(foldername)
            
            # Create the log file.
            with open(logF, 'w') as logfile:
                print("\nLog created.")
                
                # Create the file
                print("\nSplitting File...")
                
                pbar = tqdm(total = len(chunk_size_list),bar_format='{l_bar}{bar:80}{postfix[0]}',postfix=['|'])          
                while( len(chunk_size_list) != 0 ):
                    count, chunk_size = random_count_list.pop(), chunk_size_list.pop()
                    
                    # Write the part file.
                    with open(count, 'wb') as fpart:
                        data = main_file.read(chunk_size)
                        fpart.write(data)
                    
                    # Write the real sequence.
                    logfile.write(count + "\n")

                    #Update progressbar.
                    pbar.update(1)
                
                # Close the progressbar.
                pbar.close()
            chdir(testfiles_folder_path)
        # Create the Key File:
        key = [filename.split('.')[0], logF, filename.split(".")[1]]
        
        
        print("\nFile Splitted to", foldername)
        return foldername, '\n'.join(key)
    except Exception:
        print("\nFailed!")
        print_exc()


#It zips files in random order, into a .locked file.
def zipFileMaker(folder):
    try:
        zipFileName = folder[:folder.index(".")] +".locked"
        zipFileName = locked_folder_path+zipFileName
        curr_path = getcwd()
        with ZipFile(zipFileName,'w', ZIP_STORED) as zipF:
            print("Lock file created...\n")
            #print("\nZipFile created...\n")
            chdir(folder)
            files = listdir()
            
            # Progressbar.
            pbar = tqdm(files, bar_format='{l_bar}{bar:80}{postfix[0]}',postfix=['|'])
            
            for f in files:
                zipF.write(f)
                remove(f)
                # Update progressbar
                pbar.set_description("Writing file {}".format(f))
                pbar.update(1)

            # Close the progressbar.
            pbar.close()
            chdir(curr_path)

        # Delete the empty Folder.
        rmdir(folder)
        print("\nFolder {} Deleted.".format(folder))
        
        print("\nFiles Locked into {} file.".format(path.basename(zipFileName)))
    except Exception:
        print("\nFailed!")
        print_exc()

