#786
#Zub1Wun
#data from : https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data
#2024-06-06 Thursday 08:20 BST - Completed 230. The Great Squirrel Census Data Analysis (with Pandas!)

import pandas

# TODO : make dataframe, with Fur Colour and Count
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colours = data["Primary Fur Color"].unique().tolist()
print(colours[1:])
counted = data["Primary Fur Color"].value_counts()
count_dict = counted.to_dict()
colours_count = []
for colour in colours[1:]:
    print(f"There are {count_dict[colour]} of {colour} squirrels")
    colours_count.append(int(count_dict[colour]))

data_dict = {
    "Fur Colour": colours[1:],
    "Count": colours_count
}

dataFrame = pandas.DataFrame(data_dict)
dataFrame.to_csv("squirrel_count.csv")




"""
colours_list.value

count = 0
for colour in colours_list:
    for colour in colours:
        count += 1
print(f"There are {count} of {colour}")
count = 0

print(colours)
print(colours_list)
"""






"""
# TODO : Read weather_data.csv into a list called data
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file) #data_file.read().split("\n")
    print(data)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
        print(row)
    print(temperatures)
"""

"""
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# TODO : Calculate the average of temperatures
print(data["temp"].mean())
#average_temp = sum(temp_list) /len(temp_list)
#total_temp = 0
#for temp in temp_list:
#    total_temps += temp
#average_temp = total_temps / len(temp_list)
#print(average_temp)

# TODO : Find maximum value in temp
print(data["temp"].max())

# TODO : Pull out the row of data where temp is maximum
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
# TODO : Convert Monday's temperature to Fahrenheit.
fahrenheit = (monday.temp[0]) * 1.8 + 32
print(fahrenheit)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"]
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
"""