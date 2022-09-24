#imports
import csv
import os
import tkinter as tk
from tkinter import filedialog




#initialisation
##Variables
file_row = []
directory = None
n = 0
file_name = 'form.csv'
headers = ['Filename', 'Version', 'Mediatype']
#Functions

def append_list(file_name, file_row):
    with open(file_name, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(file_row)


root = tk.Tk()
root.withdraw()

with open('form.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
#main
#while true:
 #   with open('form.csv', 'a') as csvfile:
  #      writer = csv.writer(csvfile, delimiter=',')
   #     writer.write


directory = filedialog.askdirectory()
#logs the selected folder
print(directory)


for file in os.listdir(directory):
    #prints name of file
    print(file)

    append_list('form.csv', file_row)
    
