
#Import supporting Python modules
import csv
import os

#Defnie relative path of .csv file
csvpath = os.path.join('Resources','budget_data.csv')

#Initialize lists to store contents of .csv
Date=[]
Profit_Loss=[]

#Open file and read contents
with open(csvpath) as csvfile:
    
    #Create csv reader object
    csvreader = csv.reader(csvfile,delimiter=',')
    
    #Read each row of the file and store in respective lists
    for row in csvreader:
        Date.append(row[0])
        Profit_Loss.append(row[1])
