# print all pairs in array
array = [1, 2, 3, 4, 5]

def printPairs(array):
    # Nested loops are quadratic time
    for i in array: # O(n)
        for j in array: # O(n * n)
            print('Pair: {} {}').format(i, j) # O(1)

# Extended Answer: Big O(n + (n * n))
# Shorthanded Answe: Big O(n^2)
printPairs(array)