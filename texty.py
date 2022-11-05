# with open("weather_data.csv") as file:
#     contents = file.readlines()
#     print(contents)
import pandas
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row[1])
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
import numpy as np

dupa = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_ones_count = len(dupa[dupa["Primary Fur Color"] == "Gray"])
red_ones_count = len(dupa[dupa["Primary Fur Color"] == "Cinnamon"])
black_ones_count = len(dupa[dupa["Primary Fur Color"] == "Black"])
# print(grey_ones_count)
# print(red_ones_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [grey_ones_count, red_ones_count, black_ones_count]
}
# print (data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("wiewiurki.csv")
print(dupa.head(2))