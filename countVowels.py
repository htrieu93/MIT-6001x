# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 22:50:30 2018

@author: Hieu Trieu
"""

count = 0
for letter in s:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        count += 1
print("Number of vowels:" + str(count))   
 