from typing import Union
from tqdm import tqdm
from os import chdir
from pathlib import Path, PosixPath
from traceback import print_exc

from core.timerDecorator import Timer
from core.EssentialsCore import log, testfiles_folder_path, locked_folder_path


# It creates a new directory and splits a file there
# genertes a logfile
# returns the foldername
@Timer(name="Splitting process...", logger=log)
def fileSplitter(filename: PosixPath, size: int) -> Union[Path, str]:
    # Import relevant modules.
    from core.EssentialsCore import getHash, randomGenerate, randomSizeGenerate

    try:
        key = []
        logF = ""
        foldername = Path(str(filename) + "_partfiles")
        chunk_size_list = randomSizeGenerate(size)
        random_count_list = randomGenerate(len(chunk_size_list) + 1)
        print(
            "\n{} of size {} bytes will be splitted into {} parts.".format(
                filename.name, filename.stat().st_size, len(chunk_size_list)
            )
        )

        # Strart Splitting the file.
        with open(str(filename), "rb") as main_file:
            logF = random_count_list.pop()

            # Make the directory
            foldername.mkdir()
            chdir(foldername)

            # Create the log file.
            with open(logF, "w") as logfile:
                print("\nLog created.")

                # Create the file
                print("\nSplitting File...")

                pbar = tqdm(
                    total=len(chunk_size_list),
                    bar_format="{l_bar}{bar:80}{postfix[0]}",
                    postfix=["|"],
                )
                while len(chunk_size_list) != 0:
                    count, chunk_size = random_count_list.pop(), chunk_size_list.pop()

                    # Write the part file.
                    with open(count, "wb") as fpart:
                        data = main_file.read(chunk_size)
                        fpart.write(data)

                    # Write the real sequence.
                    logfile.write(count + "\n")

                    # Update progressbar.
                    pbar.update(1)

                # Close the progressbar.
                pbar.close()

        # Create the Key File:
        _filename = filename.stem
        _ext = filename.suffix
        key = [_filename, _ext, logF, getHash(logF)]

        print("\nFile Splitted to", foldername)
        chdir(testfiles_folder_path)
        return foldername, "\n".join(key)

    except Exception:
        print("\nFailed!")
        print_exc()


# It zips files in random order, into a .locked file.
def zipFileMaker(folder) -> None:
    # Import relevant modules.
    from os import listdir, remove

    try:
        # Import relevant Modules.
        from zipfile import ZipFile, ZIP_STORED

        zipFileName = folder.stem + ".locked"
        zipFileName = locked_folder_path.joinpath(zipFileName)
        with ZipFile(str(zipFileName), "w", ZIP_STORED) as zipF:
            print("Lock file created...\n")
            chdir(folder)
            files = listdir()

            # Progressbar.
            pbar = tqdm(files, bar_format="{l_bar}{bar:80}{postfix[0]}", postfix=["|"])

            for f in files:
                zipF.write(f)
                remove(f)
                # Update progressbar
                pbar.set_description("Writing file {}".format(f))
                pbar.update(1)

            # Close the progressbar.
            pbar.close()
            chdir(testfiles_folder_path)

        # Delete the empty Folder.
        folder.rmdir()
        print("\nFolder {} Deleted.".format(folder))

        print("\nFiles Locked into {} file.".format(zipFileName.name))
    except Exception:
        print("\nFailed!")
        print_exc()
