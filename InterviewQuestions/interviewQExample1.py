# Given 2 arrays, create a function that let's a user know
# (true/false) whether these two arrays contain any common items

# Example: 
# arrOne = ['a', 'b', 'c', 'x']
# arrTwo = ['z', 'y', 'i']
# Should return false;
# ============================
# arrOne = ['a', 'b', 'c', 'x']
# arrTwo = ['z', 'y', 'x']
# Should return true;

# 2 parameters - both are arrays - with no size limits 
# Should return boolean
# Ask for edge cases/clarifications

exampleArrOne = ['a', 'b', 'c', 'x']
exampleArrTwo = ['z', 'y', 'x']

# Brute force solution
def hasCommonItem(arrOne, arrTwo):
    # Brute force method would be to create a nested loop, which would have Quadratic time (O(n^2))
        # Attempt to avoid using nested loops as much as possible
    for itemOne in arrOne: # Time: O(n), Space: O(1)
        for itemTwo in arrTwo: # Time: O(n), Space: O(1)
            if itemOne is itemTwo:
                return True
    return False

print(hasCommonItem(exampleArrOne, exampleArrTwo)) # Time Complexity O(n^2), Space Complexity - O(1)

# Usually if nested loops are involved in Brute force attack then Hash Tables are most likely involved for
# finding out the most optimal solution

# Hash table solution
def hasCommonItemHashTable(arrOne, arrTwo):
    # Rather than nesting a loop, instead convert array into HashTable and then loop
    # second array to check if the HashTable at key: itemTwo is equal to true(if exists)

    # Hash table structure {
    # letter/element: true,
    # letter/element: true,
    # ...
    # }
    commonTable = {} # Initialize an object or a dict in Python for HashTable
    for itemOne in arrOne: # Time: O(n), Space: O(1)
        commonTable[itemOne] = True

    for itemTwo in arrTwo: # Time: O(m), Space: O(1)
        try: # Check HashTable or Python dictionary if key exists
            if (commonTable[itemTwo] is True):
                return True
        except: # If key is not in HashTable then Python Dictionary will throw error
            # So try/catch is necessary
            continue
    return False

print(hasCommonItemHashTable(exampleArrOne, exampleArrTwo)) # Time Complexity: O(n), Space Complexity: O(1)


