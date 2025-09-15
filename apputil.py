import seaborn as sns
import pandas as pd


# update/add code below ...
def fib_rec(n):
    if n<=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib(n):
    fib_series = [fib_rec(i) for i in  range(n+1)]
    print(fib_series)
    return(fib_series[n])