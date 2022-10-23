from shutil import move
from os import listdir, path, mkdir, remove
from tkinter.filedialog import askdirectory

# define downloads folder path
print("Please select your downloads folder")
DOWNLOADS = askdirectory()

FILE_LIST = []
EXTENSION_LIST = []

# create a list of all the files in the specified folder
def create_lists():
    for file in listdir(DOWNLOADS):
        FILE_LIST.append(file)

    # create a list of all file extensions that are in the file list created above
    for item in FILE_LIST:
        item_extension = item.split('.')[-1]
        # if the file extension is not in the list add it, otherwise do nothing
        if EXTENSION_LIST.count(item_extension) < 1:
            EXTENSION_LIST.append(item_extension)

# create folders for each type of file extension
def create_folders():
    for extension in EXTENSION_LIST:
        destination = f"{DOWNLOADS}/{extension}"
        # check if directory exits. If it doesn't, then create it
        if path.isdir(destination):
            continue
        else:
            mkdir(destination)

# move each file to the folder with the name of it's extension
def move_files():
    for file in FILE_LIST:
        source = f"{DOWNLOADS}/{file}"
        file_type = file.split('.')[-1]
        destination = f"{DOWNLOADS}/{file_type}"

        # try to move the file into it's folder
        try:
            move(source, destination)
        # if it fails
        except:
            try:
                remove(source)
            except:
                print(f"{source} is currently in use by a process.")
                input("Press any key to continue")
                continue

def main():
    create_lists()
    create_folders()
    move_files()

if __name__ == "__main__":
    main()