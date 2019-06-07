# Merge 2 given sorted arrays such that the new array is also sorted array
# Example: [0, 4, 5, 31] && [1, 4, 6, 30] => [0, 1, 4, 4, 5, 6, 30, 31]

def mergeSorted(arrOne, arrTwo):
    result = []
    currentOne = 0
    currentTwo = 0

    # loop through entire one of the arrays
    while currentOne < len(arrOne) and currentTwo < len(arrTwo):
        if arrOne[currentOne] < arrTwo[currentTwo]:
            result.append(arrOne[currentOne])
            currentOne += 1
        if arrTwo[currentTwo] <= arrOne[currentOne]:
            result.append(arrTwo[currentTwo])
            currentTwo += 1

    # loop through only if necessary
    if currentOne < len(arrOne):
        while currentOne < len(arrOne):
            result.append(arrOne[currentOne])
            currentOne += 1
    if currentTwo < len(arrTwo):
        while currentTwo < len(arrTwo):
            result.append(arrTwo[currentTwo])
            currentTwo += 1
    return result

One = [0, 4, 5, 31]
Two = [1, 4, 6, 30]
print(mergeSorted(One, Two)) # Time Complexity: O(n), Space Complexity: O(n)