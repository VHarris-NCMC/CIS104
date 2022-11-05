import time



# Name of the assignment
assignmentName = "Exercise4.0"

# Packs and Unpacks name
names = ["Victor", "Harris"] 
firstName, lastName = names
# Date
date = "10/04/2022"
# Adjusts the write speed globally
global delayFactor
delayFactor = 100

# Sets of Numbers
numbers1 = [100,24,3]
numbers2 = [12,34,45]
numbers3 = [14,10,27]

# Pauses execution, primarily to delay printing between letters
def wait(delay):
	time.sleep(float(delay/delayFactor))

# Prints slowly
# Delay = Initial Delay, before global factor
# Accelerate: Accelerates write speed per letter in a given line
# text = text line to print
def printSlow(delay=0.150, accelerate= False, *text):
	
	for word in text:

		letterCount = len(word)		#total number of letters in each word
		letterNum = 0			    # letter printed
		writeSpeedFactor = 0		# initial factor for write speed modification
		delayMax = delay			# initial delay input, can not slow down
		
		for c in word:				
			print(c, end="")		
			letterNum+=1				#increments letter counter
			if accelerate and delay > 0:	#only used for acceleration
				writeSpeedFactor = letterNum/letterCount
				writeSpeedFactor*= delayMax
			if delay > 0:
				wait(delayMax-writeSpeedFactor)	#wait between letters

# used for decoration and line spacing
#delay: delay between characters
#count: number of characters to write
#char: character used (or string, but used primarily for single characters/symbols)
def printDelay(delay=0.15, count=3, char="."):
	print("\n")
	for c in range(count):
		wait(delay)
		print(char, end="")
	print("\n")

#prints the maximum number contained in a list of 3 integers
def printMax(nums):
    
    first = str(nums[0])
    second = str(nums[1])
    third = str(nums[2])

    print ("Numbers: "+ (first) + ", " + second + ", " + third + "\n")
    maxNum = str(max(nums[0], nums[1], nums[2]))
    print("Max Number: " + maxNum +"\n")

def getNums():
    first = 0
    second = 0
    third = 0


    print("Enter a number:\n")
    first = input()
    
    print ("Numbers: "+ first + "\n")
    
    print("Enter a number:\n")
    second = input()

    print ("Numbers: "+ first + ", " + second + "\n")    
   
    print("Enter a number:\n")
    third = input()
    print ("Numbers: "+ first + ", " + second + ", " + third + "\n")
    nums = [first, second, third]
    printMax(nums)

def main():
#prints name
    printSlow(0.04, False, "\n\n  Author: " + firstName + " "+lastName, "\n")
#prints date
    printSlow(0.04, False, "\n  ", date,"\n")
#seperates author from title / text
    printDelay(0.25, 5)

#prints name of assignment
    printSlow(0.05, False, "\n\n  Assignment Name: ", assignmentName, "\n")
#prints the Question
    printSlow(0.02, True, "\n  Write a python function that takes 3 numbers as input and returns the max. Call the function 3 times with different examples.\n\n")
#indicates loading
    printDelay(delay=0.004, count=100, char='#')
    printSlow(0.02, True, "\n  Examples:\n\n")
    
    printMax(numbers1)
    
    printMax(numbers2)
    
    printMax(numbers3)

    getNums()
    getNums()
    getNums()
    
   


main()






