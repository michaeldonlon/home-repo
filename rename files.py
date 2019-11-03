#! python3

import os, tkinter, re
from tkinter import filedialog

# prompts user to choose the working directory
root = tkinter.Tk()
root.wm_title("Choose file location")
directory = tkinter.filedialog.askdirectory(title="Select location of files to rename")
root.destroy()
os.chdir(directory)
files = os.listdir(directory)

fileNameRegex = re.compile(r'(SAR-ED-)(20)(-)(\d\d)(\d\d)(.*)')
i = 33

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

    os.rename(directory + "/" + fileNameMo.group(0),
              directory + "/" + fileNameMo.group(1) + "29" + fileNameMo.group(3) +
              "04" + str(i) + fileNameMo.group(6))


#    print(directory + "/" + fileNameMo.group(0))
#    print(directory + "/" + fileNameMo.group(1) + "29" + fileNameMo.group(3) +
#              "04" + str(i) + fileNameMo.group(6))

#    print(i)
    i = i + 1

