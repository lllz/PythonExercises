def primality(help_text="Tell me a number: "):
    x = int(input(help_text))
    if x in [2,3,5,7]:
        print("This is a prime number")
    elif x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7==0:
        print("This is not a prime number")
    else:
        print("This is a prime number")
