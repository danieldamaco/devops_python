"""
Given a list of integers. Remove duplicates from the list and create a tuple. Find the minimum and maximum number.
"""
import math 
import argparse

#Getting numbers form de user
parser = argparse.ArgumentParser(description='List of numbers')
parser.add_argument('-value', nargs='+', help='Lista de valores', required=True)

#Parsing Namespace format to list 
numbersList = parser.parse_args().value

#Deleting duplicates (set) and changing to list type. 
setList = set(numbersList)
numbersCleaned = list(setList)

print("Min: ", min(numbersCleaned), "Max: ", max(numbersCleaned), "Tupla: ", tuple(numbersCleaned))