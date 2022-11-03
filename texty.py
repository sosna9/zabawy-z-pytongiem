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

dupa = pandas.read_csv("weather_data.csv")

print(dupa[dupa.temp > 15])
