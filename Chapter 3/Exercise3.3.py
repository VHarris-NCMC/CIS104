
# Packs and Unpacks name
names = ["Victor", "Harris"] 
firstName, lastName = names
# Date
date = "11/05/2022"
# Name of the assignment
assignmentName = "Exercise 3.3"
# Assignment Description / Quesion
assignmentDescription = "Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table: "



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
            #Get grade as input
            grade = float(input("\n Input Hours: "))

            if 0.0 <= grade <= 1.0:
                break
            print("Bad score")
        except:
            print("Bad score")
    

    if grade >= 0.9: 
        print("A")
    elif grade >= 0.8: 
        print("B")
    elif grade >= 0.7: 
        print("C")
    elif grade >= 0.6: 
        print("D")
    elif grade < 0.6:
        print("F")
    

    
    


main()






