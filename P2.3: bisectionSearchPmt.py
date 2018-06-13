"""
Week 2 Problem Set - Problem 3
You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)
Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!
"""
_balance = balance
monthlyInterestRate = annualInterestRate/12.0
monthlyPaymentLower = balance/12.0
monthlyPaymentUpper = (balance * (1 + monthlyInterestRate)**12)/12.0

while _balance != 0:
    _balance = balance
    month = 0
    monthlyPaymentMid = (monthlyPaymentLower + monthlyPaymentUpper)/2
    
    while month < 12:
        month = month + 1
        unpaidBalance = _balance - monthlyPaymentMid
        updatedBalance = unpaidBalance + monthlyInterestRate * unpaidBalance
        _balance = updatedBalance
    
    if _balance <-0.01:
        _balance = balance
        monthlyPaymentUpper = monthlyPaymentMid    
        monthlyPaymentMid = (monthlyPaymentLower + monthlyPaymentUpper)/2
    elif _balance > 0.01:
        _balance = balance
        monthlyPaymentLower = monthlyPaymentMid
        monthlyPaymentMid = (monthlyPaymentLower + monthlyPaymentUpper)/2
    else:
        break
print("Lowest Payment: " + str(round(monthlyPaymentMid,2)))
