def class_marks(class_list):
    print ("This is the list of all the students and their grades")
    for key in class_list:
        print (key.capitalize(), "-", class_list[key])

    print("")
    print("This is the rank of the top three students and their grades")
    sorted_list = sorted(class_list, reverse = True)
    rank = 0
    for el in sorted_list[0:3]:
        rank +=1
        print (el.capitalize() + ", you are #" + str(rank))

    print("")
    print("Here come the rewards!")
    print (sorted_list[0].capitalize()+", you got $500")
    print(sorted_list[1].capitalize() + ", you got $300")
    print(sorted_list[2].capitalize() + ", you got $100")

    print("")
    for student in class_list:
        if class_list[student] >=950:
            print ("Congratulations for being such an exceptionally good student and scoring above 950, ", student.capitalize())




first_class = {"john":780, "mary":850, "bill":560, "mike":960, "george":450}

class_marks(first_class)