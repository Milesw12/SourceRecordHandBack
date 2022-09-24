#imports
import csv


#initialisation
file_row = []
def append_list(file_name, list_of_elem):
    with open(file_name, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(list_of_elem)

#main
#while true:
 #   with open('form.csv', 'a') as csvfile:
  #      writer = csv.writer(csvfile, delimiter=',')
   #     writer.write



append_list('form.csv', file_row)