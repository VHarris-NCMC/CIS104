
# Packs and Unpacks name
names = ["Victor", "Harris"] 
firstName, lastName = names
# Date
date = "11/05/2022"
# Name of the assignment
assignmentName = "Exercise 7.3"
# Assignment Description / Quesion
assignmentDescription = "Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist. Here is a sample execution of the program:"

funnyMessage = "This is a funny message"

def begin():
#prints name / date
    print(" ", firstName, lastName, " --- ", date)
#prints name of assignment
    print("\n  Assignment Name: ", assignmentName)
#prints the Question
    print("\n ", assignmentDescription, "\n")

def getSpamAverage(fileName):
    
    # Filters to search for in file
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
    while True:
        try: 
            fileInput = input("Enter a file name (textdoc.txt): ")
            if fileInput == 'na na boo boo':
                    print(funnyMessage)
                    continue
            getSpamAverage(fileInput)
        except:
            print("Invalid file name")
  


main()






