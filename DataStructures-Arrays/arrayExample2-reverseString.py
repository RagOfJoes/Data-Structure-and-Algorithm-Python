# Create a function that reverses a string
# Example: "Hi my name is Victor"
# Reversed: "rotciV si eman ym iH"

def reverseString(input): 
    # Brute Force method
    rev = [] # Space O(n)
    for i, value in enumerate(input): # Time O(n)
        try:
            rev.append(input[-1 * (i + 1)]) # Time O(1)
        except:
            break
    return "".join(rev) # Time O (n)
        

    # Fastest solution
    # return input[::-1] # Python slicing technique(Not very readable)

    # Second Fastest (most likely)
    # return "".join(reversed(input)) # reversed() iterates through object in reverse
    # .join converts reversed object back to string again

print(reverseString("Hi my name is Victor"))