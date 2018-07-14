def reversesen():
    x = input ("Tell me a sentence ")
    y = x.split()
    result = ""
    for i in y[::-1]:
        result = result + i +" "
    return result
