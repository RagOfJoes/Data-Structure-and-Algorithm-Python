def bigOExample1(input):
    a = 10 # O(1)
    a = 50 + 3 # O(1)

    for num in input: # O(n), loops are always linear time
        anotherFunction() # O(n), because it's called for ever element
        stranger = True # O(n), same as above
        a += 1 # O(n), same as line 6
    
    return a # O(1)

# Extended answer: Big O(3 + 4n)
# Shorthand answer: Big O(n)

print(bigOExample1([1, 2, 3, 4, 5, 6]))