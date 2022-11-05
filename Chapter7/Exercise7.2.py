
# Packs and Unpacks name
names = ["Victor", "Harris"] 
firstName, lastName = names
# Date
date = "11/05/2022"
# Name of the assignment
assignmentName = "Exercise 7.2"
# Assignment Description / Quesion
assignmentDescription = "Write a program to prompt for a file name, and then read through the file and look for lines of the form:"


def begin():
#prints name / date
    print(" ", firstName, lastName, " --- ", date)
#prints name of assignment
    print("\n  Assignment Name: ", assignmentName)
#prints the Question
    print("\n ", assignmentDescription, "\n")

def getSpamAverage(fileName):
    
    filter = "X-DSPAM-Confidence: "
    count = 0
    total = 0
    docHandle = open(fileName)
    for line in docHandle:
        if line.startswith(filter):
            
            index = line.find(filter)
            index += len(filter)
            num = line[index:]
            val = float(num)
            count += 1 
            total += val

    average = total / count
    print("Count:", count)
    print("Average spam confidence: ", average)
def main():

    begin()
    fileInput = input("Enter a file name (textdoc.txt): ")
    getSpamAverage(fileInput)
  


main()






