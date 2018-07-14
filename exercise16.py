import random

def passwordgen():
    x = input ("How strong do you want your password to be: weak or strong? ")

    if x == "weak":
        print ("Here's your passowrd: ")
        return (random.choice(["cat", "pigeon", "birdy", "mouse", "parrot",]) + random.choice(["cat", "pigeon", "birdy", "mouse", "parrot",]))

    elif x == "strong":
        digits = '0123456789'
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        symbols = "!#$%&\()*+,-./:;?@[]^_`{|}~"
        print("Here's your passowrd: ")
        d = "".join(random.sample(set(digits), 3))
        l = "".join(random.sample(set(lower), 3))
        u = "".join(random.sample(set(upper), 3))
        s = "".join(random.sample(set(symbols), 3))
        password = list(d+l+u+s)
        return "".join(random.sample(set(password), 12))
