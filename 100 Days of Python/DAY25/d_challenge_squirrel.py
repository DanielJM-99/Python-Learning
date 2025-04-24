import pandas 

# Create a CSV with the sum of the fur colors (Primary Fur Color) in a small table 

# Read data
squirrel_data = pandas.read_csv("./100 Days of Python/DAY25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Only select required column
fur_colors = squirrel_data["Primary Fur Color"]

# Easier way
#unique_count_data = fur_colors.value_counts()

# Converto into list
colors_list = fur_colors.to_list()

# Get unique values
unique_colors = list(set(colors_list))
print(unique_colors)

# Count unique values and create ditionary
color_dictionary = {}
for color in unique_colors:
    if pandas.isna(color):
        pass
    else:
        color_count = colors_list.count(color)
        color_dictionary[color] = color_count
print(color_dictionary)

# Create dataframe then csv
count_data = pandas.DataFrame([color_dictionary])
print(count_data)
count_data.to_csv("squirrel_colors.csv")

# Create dataframe2 then csv
# count_data = pandas.DataFrame([unique_count_data])
# print(count_data)