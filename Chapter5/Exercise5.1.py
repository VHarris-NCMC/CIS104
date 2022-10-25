import time



assignmentName = "Exercise5.1"

# Packs and Unpacks name
names = ["Victor", "Harris"] 
firstName, lastName = names
# Date
date = "10/18/2022"
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
##def printMax(nums):
    
 
    

##def getNums():



def main():

    printSlow(0.04, False, "\n\nAuthor: " + firstName + " "+lastName+"\n")    
    printSlow(0.04, False, assignmentName+"\n")
    printSlow(0.04, False, date+"\n")
   
    

    total = 0
    count = 0
    average = 0

    while True:
    
        num = input("Enter a number: ")
    
    
        if num == "done":   
     
            break
        
        try:
        
            x = int(num)
            count = count+1
            total = total+x
            average = total / count
        except: 
            print("Invalid input") 
    
    print("\n\n\n")
    print("Total: ", total)
    print("Count: ", count) 
    print("Average: ", average) 

    
   


main()