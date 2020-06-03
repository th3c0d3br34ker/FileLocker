from pathlib import Path
from zipfile import ZipFile
from wget import download

def folderSetup():
    path = Path(".").resolve()
    (path / "TestFiles").mkdir(exist_ok=True)
    (path / "Locked").mkdir(exist_ok=True)
    (path / "Output").mkdir(exist_ok=True)
    print("Folder Setup Done!\n")

def downloadTestFiles():
    link="https://www.dropbox.com/sh/hm6vifykzmi50y9/AABu0OFQJ1zTbUiWgIjxb9iDa?dl=1"
    testfiles_path = Path("./TestFiles")
    download(link, str(testfiles_path / "TestFiles.zip"))
    print("\nExtracting...\n")
    with ZipFile(str(testfiles_path / "TestFiles.zip"), "r") as zip:
        zip.extractall(path=testfiles_path)
    (testfiles_path / "TestFiles.zip").unlink()
    print("Done!\n")

folderSetup()
downloadTestFiles()