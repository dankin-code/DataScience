# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here

opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]



# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again

for line in moma:
    nationality = line[2]
    nationality = nationality.replace("(","")
    nationality = nationality.replace(")","")
    line[2] = nationality
    gender = line[5]
    gender = gender.replace("(","")
    gender = gender.replace(")","")
    line[5] = gender


# remove empty spaces and handle missing data

for line in moma:
    
    gender = line[5]
    gender = gender.title()
    if not gender:
        gender = "Gender Unknown/Other"
    line[5] = gender
    
    nationality = line[2]
    nationality = nationality.title()
    if not nationality:
        nationality = "Nationality Unknown"
    line[2] = nationality


# clean and convert year column

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date


for line in moma:
    begin_date = line[3]
    begin_date = clean_and_convert(begin_date)
    line[3] = begin_date
    end_date = line[4]
    end_date = clean_and_convert(end_date)
    line[4] = end_date


# remove unwanted characters in a string

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(the_string_to_clean):
    for char in bad_chars:
        the_string_to_clean = the_string_to_clean.replace(char, "")
    return the_string_to_clean

stripped_test_data = []
for data in test_data:
    data = strip_characters(data)
    stripped_test_data.append(data)




test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

    
def process_data(string_date):
    if "-" in string_date:
        dates = string_date.split("-")
        int_dates = []
        for date in dates:
            integer_date = int(strip_characters(date))
            int_dates.append(integer_date)
        # get average
        sum_date = 0
        count_date = 0
        for date in int_dates:
            sum_date = sum_date + date
            count_date = count_date + 1
        average_date = round(sum_date / count_date)
        return average_date
    return int(strip_characters(string_date))
        

processed_test_data = []
for item in stripped_test_data:
    processed_test_data.append(process_data(item))
    
    
# date_date = []    
for line in moma:
    date_data = line[6]
    # new_date = strip_characters(date)
    line[6] = process_data(date_data)
    