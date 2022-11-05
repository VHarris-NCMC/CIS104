import time



assignmentName = "Exercise6 All Exercises"

# Packs and Unpacks name
names = ["Victor", "Harris"] 
firstName, lastName = names
# Date
date = "10/25/2022"
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


## Exercise 1
def Exercise1():
    sentence = "Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards."
    
    
    print("\n\n" + sentence)   
    print("\n\n Demonstration: \n\n")
   
    index = len(sentence) - 1
    printIndex = 1
    while index > 0:
        y = sentence[index]
        index -= 1
        end = ""
        if printIndex % 100 == 0:
            end ="\n"
        printIndex+=1
        print(y, end=end)
    print("\n\n")

## Exercise 2
def Exercise2():
    
    sentence = "Exercise 2: Given that fruit is a string, what does fruit[:] mean?"
  
    print("\n\n" + sentence)   
    answer = "\nAnswer: in this scenario, fruit[:] means the entire length of the string, because the ommision of the first index indicates the start of the string. Similarly, by omitting the index after the colon, this means the end of the string \n"
    print(answer)

##Exercise3
def Exercise3():
    
    sentence = "Exercise 2: Given that fruit is a string, what does fruit[:] mean?"
    print("\n\n" + sentence)   
    
    print("\n word = 'banana' \n")
    print("\ncount = 0\n")
    print("   for letter in word:")
    print("      if letter == 'a':")
    print("         count = count +1")
    print("\n print(count")        

    answer = "\nAnswer: \n\n\n"
    print(answer)

    print("def count(word, let):")
    print("\n   count = 0\n")
    print("   for letter in word:")
    print("      if letter == let:")
    print("         count = count +1")
    print("\n   print(count)\n\n")   


## Exercise4
def Exercise4():
    question = "There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method at:\n\nhttps://docs.python.org/library/stdtypes.html#string-methods\n\nWrite an invocation that counts the number of times the letter a occurs in “banana”."
    print(question)

    answer = "Answer: bananaWord.count(a)"
    print("\n" + answer)


##function used in Exercise 5

def demonstration5():
    text = "X-DSPAM-Confidence:0.8475"

    num = text.find(":")
    flt = float(text[num+1:])
    print(flt)

## Exercise5
def Exercise5():
    question = "Exercise 5: Take the following Python code that stores a string:\n\nstr = 'X-DSPAM-Confidence:0.8475'\n\nUse find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number."
    print(question)
    
    answer = "Answer: \n text = \"X-DSPAM-Confidence:0.8475\", \n num = text.find(\":\") \n flt = float(text[num+1:]) \n print(flt) \n"
    print(answer)

    print("Demonstration:\n\n")

    demonstration5()

## Exercise6
def Exercise6():
    question = "Exercise 6: Read the documentation of the string methods at https://docs.python.org/library/stdtypes.html#string-methods You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful."
    print(question)
   



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
   

    while(True):
        
        selector = input("Choose an Exercise (1, 2, 3, 4, 5, 6) or \"done\" to end:")

        if selector == "done":
            break

        try: 
            x = int(selector)

            if x == 1: 
                Exercise1()
            if x == 2: 
                Exercise2()
            if x == 3: 
                Exercise3()
            if x == 4: 
                Exercise4()
            if x == 5: 
                Exercise5()
        except:
            print("Invalid Input")
    


main()

    



    