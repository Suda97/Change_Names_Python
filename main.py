import os

if __name__ == '__main__':
    path = input("Path to change all files names (do not end it with the slash): ")
    path = path + "/"
    rename = input("New name for all the files: ")
    ext = input("File extension (leave blank if don't needed): ")
    if ext != "":
        ext = "." + ext
    ls = os.listdir(path)
    count = 0
    for i in ls:
        os.rename(path + i, path + rename + str(count) + ext)
        count += 1



