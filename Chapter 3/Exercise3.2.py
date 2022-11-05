
# Packs and Unpacks name
names = ["Victor", "Harris"] 
firstName, lastName = names
# Date
date = "11/05/2022"
# Name of the assignment
assignmentName = "Exercise 3.2"
# Assignment Description / Quesion
assignmentDescription = "Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. "


def begin():
#prints name / date
    print(" ", firstName, lastName, " --- ", date)
#prints name of assignment
    print("\n  Assignment Name: ", assignmentName)
#prints the Question
    print("\n ", assignmentDescription, "\n")


    
def main():

    begin()

    while(True):
        try: 
            #Get hours as input
            hours = float(input("\n Input Hours: "))
            #Get rate as input
            rate = float(input("\n Input Rate: "))
            break
        except: 
            print ("Error, please enter numeric input")
    
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






