"""
Week 1 Problem Set - Problem 1 
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
"""

count = 0
for letter in s:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        count += 1
print("Number of vowels:" + str(count))   
 
