# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20220957
# Date: 11/26/2023

import datetime
import os

# Creating the file path
now = datetime.datetime.now()
filename = now.strftime("%Y_%m_%d_%H_%M") + "_prog_data.txt" # https://www.programiz.com/python-programming/datetime/strftime

# Write data to the file
def write_file(data):
    with open(filename, "a") as f:
        f.write(",".join(map(str, data)) + "\n")

# Read data from the file
def read_file():
    progression_data = []

    try:
        with open(filename, "r") as r:
            lines = r.readlines()
            for i in lines:
                data = i.strip().split(',')
                progression_data.append(data)
                
    except FileNotFoundError:
        print("No progression data has been saved")

    return progression_data