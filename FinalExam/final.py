
## Victor Harris 
## final.py 
## CIS-104A 
## 12/13/22
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
        
    count = len(nums)
    sum =  getTotal(nums)
    average = sum / count

    print("Count: " + str(count) + ",\nSum: " + str(sum) + ",\nAverage: "+ str(average))

main()