
# Packs and Unpacks name
names = ["Victor", "Harris"] 
firstName, lastName = names
# Date
date = "11/05/2022"
# Name of the assignment
assignmentName = "Exercise 3.1"
# Assignment Description / Quesion
assignmentDescription = "Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours."


def begin():
#prints name / date
    print(" ", firstName, lastName, " --- ", date)
#prints name of assignment
    print("\n  Assignment Name: ", assignmentName)
#prints the Question
    print("\n ", assignmentDescription, "\n")


    
def main():

    begin()

    hours = input("\n Input Hours: ")

    rate = input("\n Input Rate: ")
    print(hours, rate)


main()






