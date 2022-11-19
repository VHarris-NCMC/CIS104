
## path to file
path = "cheeses.txt"


## Beginning
def main():


## Open a handle for Cheeses.txt
    fhand = open(path)


## Declare a list
    cheeses = []


## For each line
    for line in fhand:
    ## For each line -- yes
        
        ## Split the line 
        linecheeses = line.split()
    
        ## for each cheese in the line 
        for cheese in linecheeses: 

            ## Append to list 
                cheeses.append(cheese)


## For each line -- no (finished)
    ##sort your cheese list
    cheeses.sort()
    ## print contents of list
    print(cheeses)
    
## end


main()