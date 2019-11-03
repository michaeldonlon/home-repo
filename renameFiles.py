#! python3

import os, tkinter, re
from tkinter import filedialog

# prompts user to choose the working directory
root = tkinter.Tk()
root.wm_title("Choose file location")
directory = tkinter.filedialog.askdirectory(title="Select location of files to rename")
root.destroy()
os.chdir(directory)
# get a list of files in the cwd
files = os.listdir(directory)

# this is a pretty specific regex but it's a start for future scripts
fileNameRegex = re.compile(r'(SAR-ED-)(20)(-)(\d\d)(\d\d)(.*)')

# initialise any iterating strings to go in the filename here
i = 33

# iterate through the files
for item in files:
    fileName = str(item)
    fileNameMo = fileNameRegex.search(fileName)
#    print(fileNameMo.group(0))
#    print(fileNameMo.group(1))
#    print(fileNameMo.group(2))
#    print(fileNameMo.group(3))
#    print(fileNameMo.group(4))
#    print(fileNameMo.group(5))
#    print(fileNameMo.group(6))

#    try change the first line below to this:
#    os.rename(directory + "/" + fileName,
    os.rename(directory + "/" + fileNameMo.group(0),
              directory + "/" + fileNameMo.group(1) + "29" + fileNameMo.group(3) +
              "04" + str(i) + fileNameMo.group(6))

    i = i + 1
