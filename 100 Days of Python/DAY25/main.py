# with open("./100 Days of Python/DAY25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

# with open("./100 Days of Python/DAY25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     print(data)

    # for row in data:
    #     print(row)
    #     temperatures.append(row[1])

    # new_temps = []
    # for nums in temperatures[1:]:
    #     new_temps.append(int(nums))
    # print(new_temps)

    # for row in data:
    #     if row[1] != "temp":
    #         temperatures.append(int(row[1]))
    # print(temperatures)

import pandas

data = pandas.read_csv("./100 Days of Python/DAY25/weather_data.csv")
# print(type(data))
# print(data["temp"])

# My own exercise
nyl_data = pandas.read_csv("ECS_Ops Active Changes for the Next 10 Days.csv")
type_data = nyl_data.Type
third_row = nyl_data[nyl_data.Number == "CHG0189096"]
print(nyl_data)
print(type_data)
print(third_row)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list) / len(temp_list)
# print(round(avg_temp, 2))

print(data["temp"].mean())
print(data["temp"].max())
max_temp = data["temp"].max()
# Get data by columns
# data["column"]
# OR
# print(data.temp)

# Get data by rows with filters Table[table.column == "row_attribute"]
print(data[data.day == "Monday"])
print(data[data.temp == max_temp])

# Specific values of rows
monday = data[data.day == "Monday"]

# Convert specific values
temp_in_cels = monday.temp[0]
farenheit = (temp_in_cels * 9/5) + 32
print(farenheit)

# Create a dataframe from scratch 
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score" : [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
print(new_data)

