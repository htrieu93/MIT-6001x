"""
Week 2 Problem Set - Problem 1
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. 
"""
month = 0
monthlyInterestRate = annualInterestRate/12.0

while month < 12:
    month = month + 1
    minMonthlyPayment = monthlyPaymentRate * balance
    unpaidBalance = balance - minMonthlyPayment
    updatedBalance = unpaidBalance + monthlyInterestRate * unpaidBalance
    balance = updatedBalance
print("Remaining balance: " + str(round(balance,2)))
