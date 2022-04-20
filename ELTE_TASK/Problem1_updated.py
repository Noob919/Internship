#Importing required libraries
import numpy as np
import pandas as pd

#Read the txt file into the pandas DataFrame using read_csv method of pandas
data = pd.read_csv('input.txt', sep= ' ',header = None, names = ['Name_of_the_airline','Destination','Number_of_passengers'])

#Exercise 1
destination_list = data['Destination'] #Here we read pandas series into the variable name destination
i = 0 #Set the variable i = 0
for j in range(len(data['Destination'] == 'Frankfurt')):# we run this for loop upto the length of destination series
  if(destination_list[j] == 'Frankfurt'):#Check this condition 
    i = i+1 #If the above condition is true then update the value of variable i
print(f"{i}\0") #print the value of i


#Exercise 2
#In this excerise we try and except concept.
try: 
  df = data.sort_values(by = "Number_of_passengers", ascending = False, inplace = True)#Sort the dataframe with respect to the Number of passengers column in descending order.
  name_of_the_airline = data['Name_of_the_airline'].iloc[0] # Store the 0 index value of name of the airline column in the variable name_of_the_airline
  destination = data['Destination'].iloc[0]# Store the 0 index value of Destination column in the variable called destination
  number_of_passenger = data['Number_of_passengers'].iloc[0]# Store the 0 index value of number of passengers column in the variable called number_of_passengers
  print(f"{name_of_the_airline} {destination} {number_of_passenger} \0")#print the values using print statement
except IndexError:# if the program encounter IndexError then print the necessary statement. This will execute if we have empty dataframe
  print("This file is empty \0")

#Exercise 3
#This for loop run upto the length of number_of_passengers column
for j in range(len(data['Number_of_passengers'])):
  if(data['Number_of_passengers'][j] < 100):#Check the given condition
    name_of_the_airline = data['Name_of_the_airline'][j]
    destination = data['Destination'][j]
    number_of_passenger = data['Number_of_passengers'][j]
    print(f"{name_of_the_airline} {destination} {number_of_passenger}\0")
    #If condition satisfies then we print that index values and break the loop there itself.
    break

#If the input file contain no flight less than 100 passengers then this block of code exceutes
try:
  list_passengers = list(data['Number_of_passengers'])#Convert the pandas series into the list called list_passengers
  list_passengers.sort()#Sort the given list
  if(list_passengers[0] >= 100):#Check the given condition
    print("There is no flight with passengers less than 100\0")
except IndexError:# if the program encounter IndexError then print the necessary statement. This will execute if we have empty dataframe
  print("There is no flight with passengers less than 100\0")


#Exercise 4
try:
  df2 = data.groupby(by=data['Name_of_the_airline'], axis=0).sum() #Make the pivot table of the dataframe with respect to the column called Name of the airline
  for i in range(len(df2['Number_of_passengers'])):#This loop rins upto the length of the new dataframe called df2
    if(df2['Number_of_passengers'][i] == df2['Number_of_passengers'].max()):#If the given condition satifies execute the codes given below
      name_of_the_airline = df2.index[i]
      total_number_passengers = df2['Number_of_passengers'].max()
      print(f"{name_of_the_airline} {total_number_passengers}\0")
except KeyError:# if the program encounter KeyError then print the necessary statement. This will execute if we have empty dataframe
  print("This file is empty\0")