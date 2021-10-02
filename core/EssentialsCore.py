from traceback import print_exc
from pathlib import Path
from hashlib import sha256
from pyfiglet import figlet_format

import six

try:
    import colorama

    colorama.init()
except ImportError:
    colorama = None


try:
    from termcolor import colored
except ImportError:
    colored = None

default_dir = Path.cwd()
locked_folder_path = default_dir / "Locked"
testfiles_folder_path = default_dir / "TestFiles"
output_files_folder = default_dir / "Output"


def digitBlancer(n, size=6) -> str:
    s = "0" * (size - len(str(n)))
    return s + str(n)


def randomGenerate(n) -> list:
    try:
        from random import sample

        size = len(str(n)) + 1
        count_list = sample(range(0, n), n)
        random_count_list = list(map(lambda x: digitBlancer(x, size), count_list))
        return random_count_list
    except Exception:
        print_exc()


def randomSizeGenerate(size) -> list:
    try:
        from random import randint

        size_list = []
        exp = 0.5
        while size > 0:
            tmp = randint(1, int(size ** exp))
            size_list.append(tmp)
            size = size - tmp
        return size_list
    except Exception:
        print_exc()


def cleanit():
    try:
        from os import listdir, remove
        from os.path import isdir

        print("\nCleaning Test files Folder:", testfiles_folder_path)
        files = listdir(testfiles_folder_path)

        for f in files:
            if isdir(f) and "_partfiles" in f:
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
            remove(output_files_folder.joinpath(f))

        print("\nCleaned.")

    except Exception:
        print_exc()


def getInput(inpstring="", datatype=None, options=[]):
    if datatype == int:
        options = list(map(str, options))
        print(inpstring, end="")
        inp = input()
        isnum = inp.isdigit()
        inoptions = inp in options
        while not isnum or not inoptions:
            print(" Invalid Input!")
            if not isnum:
                print(" Enter a Number")
            if not inoptions:
                print(" Enter a Number in range:", "\n ", " ".join(options))
            print(inpstring, end="")
            inp = input()
            isnum = inp.isdigit()
            inoptions = inp in options
        return int(inp)

    if datatype == str:
        print(inpstring, end="")
        inp = input()
        return inp

    if datatype == "file":
        print(inpstring, end="")
        inp = input()
        inpF = output_files_folder.joinpath(inp)
        isFile = inpF.is_file()
        while not isFile:
            print(isFile)
            print(inpstring, end="")
            inp = input()
            inpF = output_files_folder.joinpath(inp)
            isFile = inpF.is_file()

        return inpF

    if datatype == None:
        print("\n Input datatype not specified!")
        return None


def getHash(logF) -> sha256:
    data = "".encode()
    with open(logF, "rb") as file:
        data = file.read()
    return sha256(data).hexdigest()


def log(string, color="blue", font="6x9", figlet=False) -> None:
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(string, font=font), color))
    else:
        six.print_(string)


def getFileList(path: Path) -> list:
    files = []
    for i in path.glob("**/*"):
        if Path.is_file(i):
            files.append(i)

    return files
