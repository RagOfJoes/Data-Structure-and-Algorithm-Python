# Collection of numbers and find matching pair that is equal to a given sum
# Examples:
# [1, 2, 3, 9], sum = 8
# [1, 2, 4, 4], sum = 8
# Input array, Output is bool
# Repeating elements are allowed
# Elements are integer only and are can be negative

# Brute Force Solution
def hasMatchingPairBrute(arr, sum):
    # Nested loop so Time Complexity: O(n^2), Space Complexity: O(1)
    for i in arr:
        j = i + 1
        for j in arr:
            try: # try/catch for index out of range
                if arr[i] + arr[j] is sum:
                    return True
            except:
                continue
    return False

print(hasMatchingPairBrute([1, 2, 3, 9], 8)) # Time: O(n^2), Space: O(1)

# Optimal Solution
def hasMatchingPairOptimal(arr, sum):
    # Main principle is adding complementary of element onto set
    # if and only if that element has been encountered yet

    if not arr or not sum: # Check if array is empty and sum not null
        return False

    previousEncounters = set() # Create a Hash set, Space Comp: O(n)

    # Example: [1, 2, 3, 4, 5], Sum: 8
    # 0: .add(7), 
    # 1: .add(6), 
    # 2: .add(5), 
    # 3: .add(4),
    # 4: return True
    for i in arr: # Time Complexity: O(n), Space Complexity: O(1)
        if i in previousEncounters: # py set() in method has Time Comp O(1)
            # if size of input is not too large, Worst case: O(n)
            return True
        else:
            previousEncounters.add(sum - i) # Time Complexity: O(1)
    return False

print(hasMatchingPairOptimal([1, 2, 3, 4, 5], 8)) # Average case: Time: O(n), Space: O(n)
# Worst Case: Time: O(n^2), Space: O(n)