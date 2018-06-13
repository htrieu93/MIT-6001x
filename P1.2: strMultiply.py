"""
Week 1 Problem Set - Problem 2
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
"""

count = 0 
for index in range(len(s)-2):
    if s[index] == 'b':
        if s[index+1] == 'o':
            if s[index+2] == 'b':
                count += 1
print("Number of times bob occurs is:" + str(count)) 
