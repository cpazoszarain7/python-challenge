#Import the csv library to read the .csv file
#Import Counter object from collections class
import csv
import os
from collections import Counter

#Defnie relative path of .csv file
csvpath = os.path.join('Resources','election_data.csv')

#Array to store total list of votes
votes = []

#Open file and read contents
with open(csvpath) as csvfile:
    
    #Create csv reader object
    csvreader = csv.reader(csvfile,delimiter=',')
    
    #Read each row of the file and store in respective lists
    for row in csvreader:
        votes.append(row[2])
        
#Remove headers of list
votes.remove('Candidate')
