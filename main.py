#imports
import csv
from distutils.version import Version
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, showerror




#initialisation
##Variables
directory = None
name = None
version = None
filetype = None
counter = 0

n = 0
file_name = 'form.csv'
headers = ['Filename', 'Version', 'Mediatype']
sep = '_'
sep2 = '.'
extensions = ['.pdf','.dgn','.DGN', '.PDF', '.tiff', '.tif', '.TIFF', '.TIF', '.PNG', '.png', '.JPEG', '.BMP', '.JPG', '.jpeg', '.bmp', '.jpg']
ESR = ['tiff', 'tif', 'png', 'jpeg', 'bmp', 'jpg']
#Functions

root = tk.Tk()
root.withdraw()

def append_list(file_name):
    with open(file_name, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, version, filetype])
        

def Filesort(filetype1):

    if str(filetype1).lower() == 'dgn' :
        filetype = 'CAD'
    elif str(filetype1).lower() == 'pdf':
        filetype = 'PDF'
    elif str(filetype1).lower() in ESR:
        filetype = 'ESR'
    else:
        filetype = filetype1
    return filetype

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
for root, dirs, files in os.walk(directory):
    for file in files:
        print()
        if any(file.endswith(s) for s in extensions):
            counter = counter + 1
            print(counter)
        #prints name of file
            #print(file)
            name = file.split(sep, 1)[0]
            print(name)


        #version deriving
            version1 = file.split(sep, 1)
            version1 = version1[1]
            version = version1.split(sep2, 1)[0]
            print(version)


        #filetype deriving
            filetype1 = version1.split(sep2, 1)
            filetype1 = filetype1[1]
            print(filetype1)
            filetype = Filesort(filetype1)
            print(filetype)

            append_list('form.csv')
    
if counter == sum(1 for _, _, files in os.walk(directory) for f in files):
    showinfo('Info','Code run sucessfully file can be found in '+ os.getcwd() + '/form.csv')
else:
    showerror('Error', 'There was an issue with the CSV creation please review the '+ os.getcwd() + '/form.csv')