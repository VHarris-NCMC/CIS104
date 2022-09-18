import time
import os
import sys


# Name of the assignment
assignmentName = "Exercise2.0"

# Packs and Unpacks name
names = ["Victor", "Harris"] 
firstName, lastName = names
# Date
date = "09/18/2022"
# Adjusts the write speed globally
global delayFactor
delayFactor = 100


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
			if accelerate and delay > 0:	#only used for accerlation
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
	printSlow(0.02, True, "\n  At what size of a project should you start using version management software? Why?\n\n")
#indicates loading
	printDelay(delay=0.004, count=100, char='#')

#prints the Answer file to the console
	with open(os.path.join(sys.path[0], "Answer.txt"), "r") as file:
		lineNum = 1
		for line in file:
			printSlow(0.0105/lineNum, True, line)
			lineNum+=1

	printDelay(0.002, 75, '#')

# It's a great deal, really. 
	printSlow(0.002, True, "Great news! The rest of this assignment is available at full speed with a subscription.\n")
	printSlow(0.002, True, "Please Subscribe :)\n")
	print("The full answer of over 1000 words awaits, just click enter \n")


main()






