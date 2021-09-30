import click
import six
import shutil
import requests

from pyfiglet import figlet_format
from pathlib import Path
from zipfile import ZipFile

from click.decorators import command, group

from os import chdir
from traceback import print_exc
from core.dropboxUpdown import main as dropbox
from core.EssentialsCore import getInput
from core.EssentialsCore import (
    default_dir,
    locked_folder_path,
    testfiles_folder_path,
    output_files_folder,
)

try:
    import colorama

    colorama.init()
except ImportError:
    colorama = None


try:
    from termcolor import colored
except ImportError:
    colored = None


# Constants
DROPBOX_LINK = (
    "https://www.dropbox.com/sh/ks6y8p0rym1rpkb/AABASVkUY7iC3Qm6Cueiv9Tta?dl=1"
)

CURRENT_PATH = Path(".").resolve()
TEST_FOLDER = "TestFiles"
LOCKED_FOLDER = "Locked"
OUTPUT_FOLDER = "Output"


def log(string, color, font="6x9", figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(string, font=font), color))
    else:
        six.print_(string)


@group()
def cli():
    pass


@command()
def start() -> None:
    """
    Start the tool.
    Make sure you run the check command and setup the test files.
    """
    ready = (
        locked_folder_path.exists()
        and testfiles_folder_path.exists()
        and output_files_folder.exists()
    )

    if not ready:
        log(
            """ERROR:: Make sure you run the check command and setup the test files.""",
            "red",
        )
        log(
            """run            python cli.py setup-test-files""",
            "green",
        )
        exit(1)

    log(
        "\n **************************************** WELCOME **************************************** \n",
        "white",
    )
    log(" Press 1 to Hide. \n Press 2 to Recover. \n Press 3 to Exit.", "blue")
    option = click.prompt(" Enter Choice ", type=int)
    if option == 1:
        randomize()
        log("\n Thank You!", "green")
    elif option == 2:
        derandomize()
        log("\n Thank You!", "green")
    elif option == 3:
        log("\n Exiting...", "green")
        exit()
    else:
        log("\n Invalid Choice!", "red")
        exit(0)


def randomize() -> None:
    try:
        # Import relevant Modules.
        from core.fileLockCore import randomizer

        print("\nLooking for files in local directory...\n")
        chdir(testfiles_folder_path)
        print("Currently in : {}\n".format(testfiles_folder_path))
        filelist = [x for x in testfiles_folder_path.iterdir() if x.is_file()]
        n = len(filelist)
        print("List of Files :")
        for i in range(n):
            print("{0}. {1} ".format(i + 1, str(filelist[i].name)))

        # Getting the file from the user.
        filename = filelist[
            getInput(
                inpstring="\nEnter file number : ",
                datatype=int,
                options=[x for x in range(1, n + 1)],
            )
            - 1
        ]

        # Sending the file to the Program.
        randomizer(filename)
        chdir(default_dir)
    except Exception:
        print_exc()


def derandomize() -> None:
    try:
        # Import relevant Modules.
        from core.fileLockCore import derandomizer

        print("\nLooking for files in local directory...\n")
        # print("Only works with TestFiles Directory")
        chdir(locked_folder_path)
        print("Currently in : {}\n".format(locked_folder_path))
        folderlist = [x for x in locked_folder_path.iterdir()]
        n = len(folderlist)
        options = [x for x in range(1, n + 1)]
        print("List of Folders :")

        for i in range(n):
            print("{0}. {1} ".format(i + 1, folderlist[i].name))
        # Getting the folder from the user.
        foldername = folderlist[
            getInput(
                inpstring="\nEnter folder number : ", datatype=int, options=options
            )
            - 1
        ]

        # Sending the file to the Program.
        derandomizer(foldername)
        chdir(default_dir)
    except Exception:
        print_exc()


@command()
def check():
    """Check for the required folders."""
    log(
        "Files Directory : {} ...{}".format(
            testfiles_folder_path, testfiles_folder_path.exists()
        ),
        "green" if testfiles_folder_path.exists() else "red",
    )
    log(
        "Output Directory : {} ... {}".format(
            output_files_folder, testfiles_folder_path.exists()
        ),
        "green" if testfiles_folder_path.exists() else "red",
    )
    log(
        "Default Directory : {} ... {}".format(
            default_dir, testfiles_folder_path.exists()
        ),
        "green" if testfiles_folder_path.exists() else "red",
    )


@command()
def setup_test_files():
    """Download the test files and setup up the testing folder structure."""
    log("Setting up Folder Structure...", "green")
    try:
        (CURRENT_PATH / TEST_FOLDER).mkdir(exist_ok=True)
        (CURRENT_PATH / LOCKED_FOLDER).mkdir(exist_ok=True)
        (CURRENT_PATH / OUTPUT_FOLDER).mkdir(exist_ok=True)

        testfiles_path = Path("./TestFiles")
        req = requests.get(DROPBOX_LINK, stream=True)
        total_size = int(req.headers["content-length"])

        OUTPUT_FILE_PATH = str(testfiles_path / "TestFiles.zip")
        with open(OUTPUT_FILE_PATH, "wb") as OUTPUT_FILE:
            with click.progressbar(
                iterable=req.iter_content(chunk_size=1024),
                length=int(total_size / 1024),
                label="Downloading files...",
            ) as progressbar:
                for data in progressbar:
                    OUTPUT_FILE.write(data)
                    progressbar.update(n_steps=1)
        log("\nComplete.", "green")

        log("\nExtracting...", "green")
        with ZipFile(str(testfiles_path / "TestFiles.zip"), "r") as zipf:
            zipf.extractall(path=testfiles_path)
        (testfiles_path / "TestFiles.zip").unlink()
        log("Complete!\n", "green")
    except Exception:
        log("Failed to setup Folder Structure!\nAborting...", "red")
        exit(1)

    log("Folder Setup Done!\n", "green")


@command()
def remove_test_files():
    """Cleanup the testing files and directory."""
    try:
        log("Warning all progress will be lost!", "yellow")
        confirm = click.confirm("Do you want to continue?", abort=True)
        if confirm:
            log("Removing... " + TEST_FOLDER, "green")
            shutil.rmtree(CURRENT_PATH / TEST_FOLDER, ignore_errors=True)
            log("Removing... " + LOCKED_FOLDER, "green")
            shutil.rmtree(CURRENT_PATH / LOCKED_FOLDER, ignore_errors=True)
            log("Removing... " + OUTPUT_FOLDER, "green")
            shutil.rmtree(CURRENT_PATH / OUTPUT_FOLDER, ignore_errors=True)
    except Exception:
        log("Failed to remove Files!\nAborting...", "red")
        exit(1)


@command()
def add_to_dropbox():
    """Add the files in TestFiles folder to dropbox."""
    dropbox()


# Add version
click.version_option(version="v2.0.0")

# Add the commads
cli.add_command(setup_test_files)
cli.add_command(remove_test_files)
cli.add_command(add_to_dropbox)
cli.add_command(start)
cli.add_command(check)


if __name__ == "__main__":
    """CLI for setting up testing files."""
    log("Utils CLI", color="blue", figlet=True)
    log("Welcome to Utils CLI.\n", color="green")
    cli()
