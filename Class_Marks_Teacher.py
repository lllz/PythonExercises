import operator

def readStudentDetails():

    print ("Enter the number of students")
    numberOfStudents = int(input())
    studentRecord = {}
    for student in range (0, numberOfStudents):
        print("Enter the name of the student")
        name = input()
        print("Enter the marks of the student")
        marks = int(input())
        studentRecord[name] = marks
    return studentRecord

def rankStudents(studentRecord):
    try:
        sortedStudentRecord = sorted(studentRecord.items(),key=operator.itemgetter(1),reverse=True)
        print(sortedStudentRecord)
        print("{} has secured first rank, scoring {} marks".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
        print("{} has secured second rank, scoring {} marks".format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
        print("{} has secured third rank, scoring {} marks".format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
        return sortedStudentRecord
    except IndexError:
        print("Minimum 3 students")
        quit()


def rewardStudents(sortedStudentRecord, reward):
    print ("{} has received a cash reward of {}".format(sortedStudentRecord[0][0], reward[0]))
    print ("{} has received a cash reward of {}".format(sortedStudentRecord[1][0], reward[1]))
    print ("{} has received a cash reward of {}".format(sortedStudentRecord[2][0], reward[2]))

def appreciateStudents(sortedStudentRecord):
    for record in sortedStudentRecord:
        if record[1] >= 950:
            print ("Congratulations on scoring {} marks, {}".format(record[1], record[0]))
        else:
            break


studentRecord = readStudentDetails()
sortedStudentRecord = rankStudents(studentRecord)
reward = (500, 300, 100)
rewardStudents(sortedStudentRecord, reward)
appreciateStudents(sortedStudentRecord)