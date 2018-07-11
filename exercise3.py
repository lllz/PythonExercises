def listFilter(listtofilter):
    benchmark = int (input ("Give me a number: "))
    filteredlist = []
    for i in listtofilter:
        if i < benchmark:
            filteredlist.append(i)
    print (filteredlist)

