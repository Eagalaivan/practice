class LRUMemory:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}

    def get(self,key):
        if key not in self.cache:
            return -1
        value=self.cache[key]
        del self.cache[key]
        self.cache[key]=value
        return value
    def put(self,key,value):
        if key in self.cache:
            del self.cache[key]

        self.cache[key]=value

        if(len(self.cache)>self.capacity):
            self.cache.popitem()
ram = LRUMemory(2)
ram.put(1, 1)
ram.put(2, 2)
print(ram.get(1))
ram.put(3, 3) 
print(ram.get(2)) 
ram.put(4, 4)
print(ram.get(1))
print(ram.get(3))
print(ram.get(4)) 