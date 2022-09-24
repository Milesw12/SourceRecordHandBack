#imports
import csv
from distutils.version import Version
import os
import tkinter as tk
from tkinter import filedialog




#initialisation
##Variables
directory = None
name = None
version = None
filetype = None
file_row = [name, version, filetype]
n = 0
file_name = 'form.csv'
headers = ['Filename', 'Version', 'Mediatype']
sep = '_'
sep2 = '.'
#Functions

def append_list(file_name, file_row):
    with open(file_name, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(file_row)


root = tk.Tk()
root.withdraw()
#writes headers into form
with open('form.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
#main
#while true:
 #   with open('form.csv', 'a') as csvfile:
  #      writer = csv.writer(csvfile, delimiter=',')
   #     writer.write

#prompts for location of records
directory = filedialog.askdirectory()
#logs the selected folder
print(directory)

#lists documents
for file in os.listdir(directory):

#prints name of file
    #print(file)
    name = file.split(sep, 1)[0]
    print(name)


#version deriving
    version1 = file.split(sep, 1)
    version1 = version1[1]
    version = version1.split(sep2, 1)[0]
    print(version)


#filetype derviving
    filetype = version1.split(sep2, 1)
    filetype = filetype[1]
    print(filetype)

    append_list('form.csv', file_row)
    
