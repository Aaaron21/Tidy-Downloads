from shutil import move
from os import listdir, path, mkdir, remove

# define downloads folder path
DOWNLOADS = "C:\\Users\\aronk\\Downloads\\"

FILE_LIST = []
EXTENSION_LIST = []

def create_lists():
    # create a list of all the files in the specified folder
    for file in listdir(DOWNLOADS):
        FILE_LIST.append(file)

    # create a list of all file extensions that are in the file list created above
    for item in FILE_LIST:
        item_extension = item.split('.')[-1]
        # if the file extension is not in the list add it, otherwise do nothing
        if EXTENSION_LIST.count(item_extension) < 1:
            EXTENSION_LIST.append(item_extension)

def create_folders():
    # create folders for each type of file extension
    for extension in EXTENSION_LIST:
        destination = f"{DOWNLOADS}\\{extension}"
        # check if directory exits. If it doesn't, then create it
        if path.isdir(destination):
            continue
        else:
            mkdir(destination)

def move_files():
    # move each file to the folder with the name of it's extension
    for file in FILE_LIST:
        source = f"{DOWNLOADS}\\{file}"
        file_type = file.split('.')[-1]
        destination = f"{DOWNLOADS}\\{file_type}"

        # try to move the file into it's folder
        try:
            move(source, destination)
        # if it fails, remove it
        except:
            remove(source)

def main():
    create_lists()
    create_folders()
    move_files()

if __name__ == "__main__":
    main()