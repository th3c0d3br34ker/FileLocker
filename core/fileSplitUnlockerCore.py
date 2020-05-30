from os import chdir, remove
from os.path import basename
from traceback import print_exc
from core.EssentialsCore import output_files_folder, locked_folder_path, default_dir
from tqdm import tqdm


# It just Unzips the files in '_partfiles' directory.
def unZipper(filename):
    # Import relevant modules.
    from zipfile import ZipFile
    from os import mkdir

    foldername = filename.split('.')[0] + "_partfiles"
    print("\n {} will be unlocked to {}\n".format(filename, foldername))

    filename = str(locked_folder_path)+ r"/"+filename

    try:
        # Create the folder.
        chdir(output_files_folder)
        mkdir(foldername)
        foldername = str(output_files_folder)+R"/"+foldername

        with ZipFile(filename) as zipF:
            file_list = zipF.namelist()
            pbar = tqdm(total=len(file_list),
                        bar_format='{l_bar}{bar:80}{postfix[0]}', postfix=['|'])
            for f in file_list:
                zipF.extract(f, foldername)

                # Update progressbar.
                pbar.update(1)
                pbar.set_description("Unlocking file {}".format(f))

            # Close progressbar.
            pbar.close()
        # Delete the file.
        chdir(default_dir)
        remove(filename)
        return basename(foldername)

    except Exception:
        print("\nFailed!")
        print_exc()


# It joins the files in correct order
# from the log file
def fileJoiner(folder, log, ext):
    # Import relevant modules.
    from os import rmdir, listdir
    try:
        chdir(str(output_files_folder)+r"/"+folder)
        filename = str(output_files_folder) + \
            folder.replace("_partfiles", '') + '.' + ext
        with open(log, 'r') as logfile:
            print("\n Making file {}...".format(basename(filename)))
            # Create and start writing
            with open(filename, 'wb') as main_file:
                pbar = tqdm(
                    total=len(listdir()), bar_format='{l_bar}{bar:80}{postfix[0]}', postfix=['|'])
                for f in logfile:
                    with open(f.strip(), 'rb') as fpart:
                        file_obj = fpart.read()
                    main_file.write(file_obj)
                    remove(f.strip())
                    pbar.update(1)
                pbar.update()
                pbar.close()
        # Delete Logfile.
        remove(log)
        print("\n Log file deleted.")

        chdir(default_dir)

        # Delete Empty Folder
        rmdir(str(output_files_folder)+folder)
    except Exception:
        print("\nFailed!")
        print_exc()


# keyHash: Hash from the key.
# keyF: File to check with keyHash
# lockedF: '.locked' file which contains the keyF file.
def matchKey(keyHash, keyF, lockedF):
    from zipfile import ZipFile
    from hashlib import sha256
    try:
        keyF_data = None
        with ZipFile(lockedF) as zipF:
            keyF_data = zipF.read(keyF)

        if sha256(keyF_data).hexdigest() == keyHash:
            return True
        else:
            return False
    except:
        print_exc()
