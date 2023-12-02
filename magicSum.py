def magicSum(arr : list):
    magicArr = []
    
    sumLeft = 0
    subtractRight = sum(arr)
    
    for number in range(len(arr)):
        subtractRight -= arr[number]
        magicArr.append(sumLeft - subtractRight)
        sumLeft += arr[number]
    
    return magicArr


arrr = magicSum([3,5,3,4,8,0,10])
print(arrr)