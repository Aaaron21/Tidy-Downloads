import shutil
import os

# define downloads folder path
DOWNLOADS = "C:\\Users\\aronk\\Downloads\\"

FILE_LIST = []
EXTENSION_LIST = []

# create a list of all the files in the specified folder
for file in os.listdir(DOWNLOADS):
    FILE_LIST.append(file)

# create a list of all file extensions that are in the file list created above
for item in FILE_LIST:
    item_extension = item.split('.')[-1]
    # if the file extension is not in the list add it, otherwise do nothing
    if EXTENSION_LIST.count(item_extension) < 1:
        EXTENSION_LIST.append(item_extension)

# create folders for each type of file extension
for extension in EXTENSION_LIST:
    destination = f"{DOWNLOADS}\\{extension}"
    # check if directory exits. If it doesn't, then create it 
    if os.path.isdir(destination):
        continue
    else:
        os.mkdir(destination)

# move each file to the folder with the name of it's extension
for file in FILE_LIST:
    source = f"{DOWNLOADS}\\{file}"
    file_type = file.split('.')[-1]
    destination = f"{DOWNLOADS}\\{file_type}"

    # try to move the file into it's folder
    try:
        shutil.move(source, destination)
    # if it fails, remove it
    except:
        os.remove(source)