

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

genres = extract(11)

def freq_table(list_of_items):
    frequency = {}
    for item in list_of_items:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency
        
        
genres_ft = freq_table(genres)  






##################


opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(column_index, data_file):
    frequency = {}
    column = []
    for row in data_file[1:]:
        value = row[column_index]
        column.append(value)
        
    for item in column:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
            
    return frequency

ratings_ft = freq_table(7, apps_data)



# 

# INITIAL FUNCTION
def freq_table(index):
    frequency_table = {}
    
    for row in apps_data[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table