"""
Week 1 Problem Set - Problem 3
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
"""

alp = 'abcdefghijklmnopqrstuvwxyz'

max = ""
s_ = len(s)
alp_ = len(alp)
l = 0

for l in range(s_):
    strg= s[l]
    i = 0
    for i in range (alp_):
        if s[l] == alp[i]:
            for j in s[l+1:]:
                if j in alp[i:]:
                    strg = strg + j
                    i = alp.index(j)
                elif j not in  alp[i:]:
                        break 
    if len(strg) > len(max):
        max = strg
print("Longest substring in alphabetical order is: " + max)
