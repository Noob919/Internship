#Importing requiredlibraries
import numpy as np
import pandas as pd

#Read the txt file into the pandas DataFrame
data = pd.read_csv('input.txt', sep= ' ',header = None, names = ['Name of the airline','Destination','Number of passengers'])

#Example 1
destination_list = data['Destination']
i = 0
for j in range(len(data['Destination'] == 'Frankfurt')):
  if(destination_list[j] == 'Frankfurt'):
    i = i+1
print(f"{i}\0")

#Example 2
for j in range(len(data['Number of passengers'])):
  if(data['Number of passengers'][j] == (data['Number of passengers'].max())):
    name_of_the_airline = data['Name of the airline'][j]
    destination = data['Destination'][j]
    number_of_passenger = data['Number of passengers'][j]
    print(f"{name_of_the_airline} {destination} {number_of_passenger} \0")
if(data.empty ==1):
  print("This file is empty\0")

#Example 3
for j in range(len(data['Number of passengers'])):
  if(data['Number of passengers'][j] < 100):
    name_of_the_airline = data['Name of the airline'][j]
    destination = data['Destination'][j]
    number_of_passenger = data['Number of passengers'][j]
    print(f"{name_of_the_airline} {destination} {number_of_passenger}\0")
    break

try:
  list_passengers = list(data['Number of passengers'])
  list_passengers.sort()
  if(list_passengers[0] >= 100):
    print("There is no flight with passengers less than 100\0")
except IndexError:
  print("There is no flight with passengers less than 100\0")


#Example 4
try:
  df = data.groupby(by=data['Name of the airline'], axis=0).sum()
  for i in range(len(df['Number of passengers'])):
    if(df['Number of passengers'][i] == df['Number of passengers'].max()):
      name_of_the_airline = df.index[i]
      total_number_passengers = df['Number of passengers'].max()
      print(f"{name_of_the_airline} {total_number_passengers}\0")
except KeyError:
  print("This file is empty\0")