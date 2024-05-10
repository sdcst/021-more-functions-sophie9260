#!python3
"""
Create a function that calculates the amount of compound interest 
earned.
t = time in years
P = amount invested
n = # of compounding periods per year (how often interest is calculated)
Output should be rounded to 2 decimal places
r = rate of interest as a percentage
"""

def compoundInterest(P,r,t,n):
    P = float(P)
    r = float(r)
    r =  r/100
    t = float(t)
    n = float(n)
    upper = n*t
    upper = float(upper)
    middle = r/n
    Middle = 1+middle
    PP = Middle**upper
    a = P*PP
    a = float(a)
    a = round(a,2)
    return a

assert compoundInterest(1000,4,2,4) == 1082.86
assert compoundInterest(2500,4.2,20,12) == 5782.43
assert compoundInterest(83,7,5,365) == 117.78
assert compoundInterest(10000,3,10,2) == 13468.55