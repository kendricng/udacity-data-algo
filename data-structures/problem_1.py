class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.cache = dict()
        self.keys_age = dict()
        self.capacity = capacity
        self.age = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            self.keys_age[key] = self.age
            self.age += 1
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if self.capacity == 0:
            print("This cache has no capacity to set values.")
            return -1

        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if len(self.cache) == self.capacity:
            oldest_key = min(self.keys_age, 
                             key=lambda k: self.keys_age[k])
            self.cache.pop(oldest_key)
            self.keys_age.pop(oldest_key)

        # Udacity insructions say that it MUST insert the element
        self.cache[key] = value
        self.keys_age[key] = self.age
        self.age += 1

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large
# values

# Test Case 1
cache = LRU_Cache(0)
print(cache.set(4, 5)) # returns "This cache has no capacity to set values."
print(cache.get(4)) # returns -1

# Test Case 2
cache = LRU_Cache(3)
cache.set(4, "")
print(cache.get(4)) # returns ""

cache.set("", 10)
print(cache.get("")) # returns 10

cache.set(None, 1023452)
print(cache.get(None)) # returns 1023452
print(cache.get(4)) # returns ""

cache.set(6043294, 1)
print(cache.get(6043294)) # returns 1
print(cache.get(4)) # returns ""
print(cache.get("")) # returns -1 as it's the oldest cache element

# Test Case 3
cache = LRU_Cache(19534985134)
cache.set(0x34f, "abd")
print(cache.get(0x34f)) # returns "abd"
print(cache.get("abd")) # returns -1

cache.set("st", 92039483582903845902824353)
print(cache.get("st"))
print(cache.capacity) # returns 19534985134
print(cache.age) # returns 4
