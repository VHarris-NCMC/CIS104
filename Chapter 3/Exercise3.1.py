
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
    #Get hours as input
    hours = float(input("\n Input Hours: "))
    #Get rate as input
    rate = float(input("\n Input Rate: "))
    
    overtime = 0
    
    #Sets overtime if necessary
    if hours > 40:
        overtime = hours - 40
        hours = 40
    #Hours adjusted for overtime
    payableHours = hours + (overtime * 1.5)
    
    pay = payableHours * rate

    print("Pay: ", pay)
    

    
    
    


main()






