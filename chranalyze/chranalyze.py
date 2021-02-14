#!/usr/bin/env python

"""
A function to analyze characters
"""

# Chranalyze: program to analyze characters 
from string import ascii_lowercase
from string import digits
import pandas as pd
import matplotlib.pyplot as plt

def chranalyze(input_data):
    # Converts string to list and combines digits and alphabets into one list
    alphanum_list = list(digits) + list(ascii_lowercase)

    # Checks if data type is a string and returns informative message. The isinstance() function returns a boolean.
    if isinstance(input_data, str) != True:
        print("Not string")
    else: 
        print("This is a string")
        input_data = str(input_data)

    # create an empty dictionary
    chranalyzer_dict = {}

    # Counts of each alphanumeric character in the user_input are calculated
    for char in alphanum_list:
        # Counts current character from alphanum_list through input_data
        char_count = input_data.count(char)
        # Stores character and character count as a dict
        char_count_dict = {char: char_count}
        # Updates the main charanlyzer dict 
        chranalyzer_dict.update(char_count_dict)

    # Converts dictionary to stored data in table format
    #chranalyzer_table = pd.DataFrame(chranalyzer_dict.items(), columns=["character" , "count"])
    chranalyzer_series = pd.Series(chranalyzer_dict)
    chranalyzer_series = chranalyzer_series[chranalyzer_series != 0]

    # Plots table into bar chart
    chranalyzer_plot= chranalyzer_series.plot.bar(x='character', y='count', rot=0)
   
    # Create a filtered table with only characters that occured and display this in the console
    # table_with_counts = chranalyzer_table[chranalyzer_table['count'] != 0]
    series_with_counts = chranalyzer_series[chranalyzer_series != 0]
    print(series_with_counts)

    # Show plot
    plt.show()

# input_data is declared using the input function. The user is prompted to enter data which will return as lowercase. 
input_data = input("Please enter data \n").lower()

chranalyze(input_data)

if __name__ == "__main__":
    chranalyze(input_data)