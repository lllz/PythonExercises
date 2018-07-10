def numberDef():
    num1 = int(input ("Tell me a number: "))
    num2 = int(input ("Tell me another number: "))
    if num1 %4 == 0:
        print ("The number you picked is divisible by 4")
    elif num1 % 2 == 0:
        print("The number you picked is even")
    else:
        print("The number you picked is odd")

    if num1 % num2 == 0:
        print ("The two numbers that you picked are divisible without remainder")
    else:
        print ("The two numbers that you picked are not divisible without remainder")

