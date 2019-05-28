# My own implementation of an array
# Methods: get, push, pop, delete, shift
class MyArray:
    def __init__(self): # Constructor
        # Properties
        self.length = 0
        self.data = {}

    # Methods
    def get(self, index): # Time Complexity O(1)
        return self.data[index]
    
    def push(self, element): # Time Complexity O(1)
        self.data[self.length] = element
        self.length += 1

    def pop(self): # Time Complexity O(1)
        try:
            lastItem = self.get(self.length - 1)
        except:
            return "Empty!"
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem
    
    def delete(self, index): # Time Complexity O(n)
        self.shift(index)
        return self.data

    def shift(self, index): # Time Complexity O(n)
        for i, value in enumerate(self.data): # enumerate returns iterable object for 
            # retrieving inddexes and values
            if i >= index:
                try:
                    self.data[i] = self.data[i + 1]
                except:
                    break
        del self.data[self.length - 1]
        self.length -= 1
        return self.data

# Test
arr = MyArray()
arr.push(1)
arr.push(2)
arr.push(3)
arr.push(4)
print("Push: {}".format(arr.data))
arr.pop()
print("Pop: {}".format(arr.data))
print("Delete: {}".format(arr.delete(1)))
arr.push(5)
arr.push(6)
print("Shift: {}".format(arr.shift(0)))