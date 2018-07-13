import random

def commonEl():
    a = random.sample(range(0,100), 25)
    b = random.sample(range(0,100), 45)
    print(a)
    print(b)
    print ("***********" *3)
    result = []

    for i in a:
        for j in b:
            if i == j:
                if i not in result:
                    result.append(i)
    return (result)
