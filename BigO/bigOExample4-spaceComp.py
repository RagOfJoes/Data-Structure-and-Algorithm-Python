def One(num):
    for i in num: # Only creates one variable and that's it so Space Complexity: O(1)
        print(i)

One([1, 2, 3, 4, 5]) # Space Complexity: O(1)

def Two(num):
    array = [] # Creates array once O(1)
    for j in num: # O(1)
        array.insert(j, j) # Assigns value to index in array N times so Space Complexity: O(n)
    return array

print(Two([1, 2, 3, 4, 5])) # Space Complexity: O(n)