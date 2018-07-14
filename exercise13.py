def fib():
    x = int (input("How many Fibonacci numbers do you want? "))
    fiblist = [1,1]
    for i in range (1, x):
        fiblist.append((fiblist[i-1]) + fiblist[i])
    return fiblist [:-1]

