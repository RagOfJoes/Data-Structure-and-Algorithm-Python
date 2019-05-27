def bigOExample2(input):
    a = 5 # O(1)
    b = 10 # O(1)
    c = 50 # O(1)

    for num in input: # O(n)
        x = num + 1 # O(n)
        y = num + 2 # O(n)
        z = num + 3 # O(n)
    
    for num in input: # O(n)
        p = num * 2 # O(n)
        q = num * 2 # O(n)
    
    whoAmI = "I don't know" # O(1)

# Extended Answer: Big O(4 + 7n)
# Shorthand Answer: Big O(n)


