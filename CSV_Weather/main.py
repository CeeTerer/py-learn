#
# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#
# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# #print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].tolist()
# average = round(sum(temp_list) / len(temp_list))
# print(average)

# mean
# mean = data["temp"].mean()
# print(mean)
# # max
# maximum = data["temp"].max()
# print(maximum)
#
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# Create dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# dta = pandas.DataFrame(data_dict)
# print(dta)
# dta.to_csv("./CSV_Weather.csv")
#

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# squirrel_count = squirrel_data["Primary Fur Color"].value_counts()
# squirrel_count_df = pandas.DataFrame(squirrel_count)
# squirrel_count_df.to_csv("./squirrel_count.csv")

grey_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./Squirrel Count.csv")




