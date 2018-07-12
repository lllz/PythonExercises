def divisor():
    x = int(input("Please, give me a number: "))
    result = []
    for i in range (2,x):
        if x % i == 0:
            result.append(i)
    return result


