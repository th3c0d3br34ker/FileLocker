from os import chdir, mkdir, getcwd, listdir, path, remove, rmdir
from traceback import print_exc
from EssentialsCore import digitBlancer, output_files_folder, locked_folder_path, default_dir
from tqdm import tqdm


#It just splits the file in current directory.
# To become UnZipper.
def unZipper(filename):
    # Import relevant modules.
    from zipfile import ZipFile

    foldername = filename.split('.')[0] + "_partfiles"
    print("{} will be unlocked to {}\n".format(filename, foldername))

    filename = locked_folder_path+"\\"+filename 

    try:
        # Create the folder.
        chdir(output_files_folder)
        mkdir(foldername)
        foldername = output_files_folder+foldername

        with ZipFile(filename) as zipF:
            file_list = zipF.namelist()
            pbar = tqdm(total = len(file_list),bar_format='{l_bar}{bar:80}{postfix[0]}',postfix=['|'])
            for f in file_list:    
                zipF.extract(f, foldername)

                # Update progressbar.
                pbar.update(1)
                pbar.set_description("Unlocking file {}".format(f))
            
            # Close progressbar.
            pbar.close()
        #Delete the file.
        chdir(default_dir)
        remove(filename)
        return path.basename(foldername)  

    except Exception:
        print("\nFailed!")
        print_exc()



# It joins the files in correct order
# from the log file
def fileJoiner(folder, log, ext):

    try:
        chdir(output_files_folder+folder)
        filename = output_files_folder+folder.replace("_partfiles",'') +'.' + ext
        with open (log,'r') as logfile:
            print("\nMaking file {}...".format(path.basename(filename)))   
            #Create and start writing
            with open(filename,'wb') as main_file:
                pbar = tqdm(total = len(listdir()),bar_format='{l_bar}{bar:80}{postfix[0]}',postfix=['|'])
                for f in logfile:
                    with open(f.strip(),'rb') as fpart:
                        file_obj = fpart.read()
                    main_file.write(file_obj)
                    remove(f.strip())
                    pbar.update(1)
                pbar.update()
                pbar.close()
        # Delete Logfile.
        remove(log)
        print("\nLog file deleted.")

        print("\nFiles joined to {} file.".format(path.basename(filename)))
        chdir(default_dir)
        
        #Delete Empty Folder
        rmdir(output_files_folder+folder)
    except Exception:
        print("\nFailed!")
        print_exc()