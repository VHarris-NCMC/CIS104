
## Victor Harris 
## CIS-104A 
def getTotal(nums):
    
    sum = 0
    for num in nums: 
        sum += num
    return sum

def main():

    numIn = ''
    nums = []
    
    while True:

        numIn = input("Enter a numeric value, or 'quit' to exit:")
        
        if numIn == 'quit':
            break
        else:
            try:    
                 num = float(numIn)
            except:
                continue

        nums.append(num)
        
    maxi = max(nums)
    mini = min(nums)
    

    print("Max: " + str(maxi) + ",\nMin: " + str(mini))

main()