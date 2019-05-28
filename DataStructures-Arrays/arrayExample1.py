from collections import namedtuple
# Time complexity:
    # -Lookup O(1)
    # -Push O(1)
    # -Insert O(n)
    # -Delete O(n)
stringArr = ['a', 'b', 'c', 'd']
# Memory: 4 elements * 4 different "shelves" = 16 bytes

# Lookup
stringArr[3] # Time Complexity: O(1)

# Push/Append | Can be O(n) b/c Python uses dynamic arrays meaning
# it needs to expand memory. Look up Amorized Worst Case
stringArr.append('e') # Time Complexity: O(1)

# Insert
stringArr.insert(0, 0) # Time Complexity: O(n)

# Delete | All have Time Complexity: O(n)
stringArr.remove('a') # Removes first matching value in array | Throws error if not found
del stringArr[2] # Delete for specific index, Time Complexity: O(n)
stringArr.pop() # Removes and returns item at index | Throws error if empty or out of range

# Slice | [start Index:stop Index]
stringArr[0:2] # Time Complexity: O(k) - k can either be value of parameter or number of elements in parameter

print(stringArr)