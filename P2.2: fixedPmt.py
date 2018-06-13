"""
Week 2 Problem Set - Problem 2
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180 
"""
_balance = balance
monthlyInterestRate = annualInterestRate/12.0
minMonthlyPayment = 0

while _balance > 0:
    minMonthlyPayment = minMonthlyPayment + 10
    month = 0
    while month < 12:
        month = month + 1
        unpaidBalance = _balance - minMonthlyPayment
        updatedBalance = unpaidBalance + monthlyInterestRate * unpaidBalance
        _balance = updatedBalance
    if _balance <0:
        break
    else:
        _balance = balance
print("Lowest Payment: " + str(minMonthlyPayment))
