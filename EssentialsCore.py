from traceback import print_exc

locked_folder_path = "\\Locked\\"
testfiles_folder_path = "\\TestFiles\\"
default_dir = "\\FileSecurity\\"       
output_files_folder = "\\Output\\"

def digitBlancer(n, size = 6):
    s = '0' * (size-len(str(n)))
    return s+str(n)

def randomGenerate(n):
    try:
        from random import sample
        size = len(str(n))+1
        count_list = sample(range(0, n), n)
        random_count_list = list(map(lambda x : digitBlancer(x, size), count_list))
        return random_count_list
    except Exception:
        print_exc()

def randomSizeGenerate(size):
    from random import randint
    size_list = []
    exp = 0.5
    while(size>0):
        tmp = randint(1, int(size**exp))
        size_list.append(tmp)
        size = size - tmp
    return size_list



def cleanit():
    try:
        from os import listdir, remove, path
        
        print("\nCleaning Test files Folder:", testfiles_folder_path)
        files = listdir(testfiles_folder_path)

        for f in files:
            if path.isdir(f) and '_partfile' in f :
                print("Cleaing {}".format(f))
                remove(locked_folder_path + f)
        
        print("\nCleaned.")

        print("\nCleaning Locked Folder:", locked_folder_path)
        files = listdir(locked_folder_path)

        for f in files:
            print("Cleaing {}".format(f))
            remove(locked_folder_path + f)
        
        print("\nCleaned.")
    except Exception:
        print_exc()