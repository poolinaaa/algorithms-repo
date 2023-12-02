from itertools import count


def magicSum(arr: list):
    magicArr = []

    sumLeft = 0
    subtractRight = sum(arr)

    for number in range(len(arr)):
        subtractRight -= arr[number]
        magicArr.append(sumLeft - subtractRight)
        sumLeft += arr[number]

    return magicArr


arrMagic = magicSum([3, 5, 3, 4, 8, 0, 10])
print(arrMagic)

# sorting elements


def sortArr(arr):

    dictCount = {}
    for element in range(len(arr)):
        if arr[element] in dictCount:
            dictCount[arr[element]] += 1
        else:
            dictCount[arr[element]] = 1

    occurrenceList = list(set(dictCount.values()))
    sort1 = sorted(arr)
    sorted2 = []

    for i in range(len(occurrenceList)):
        for nr in range(len(sort1)):
            if dictCount[sort1[nr]] == occurrenceList[i]:

                sorted2.append(sort1[nr])

    print(sorted2)


sortArr([3, 5, 3, 4, 8, 0, 10])
