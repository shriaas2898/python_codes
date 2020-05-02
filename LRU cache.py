'''Python implementation of 
Least recently used algorithm'''
class LRUCache:
    #defining class variables
    def __init__(self, capacity: int):
        self.keys = []
        self.values = []
        self.access = []
        self.capacity = capacity
        self.access_count = 0
        
        
    '''Returns value of key supplied if key is present in cache
        if key is not present returns -1'''
    def get(self, key: int) -> int:
        if key in self.keys:
            self.access[self.keys.index(key)] = self.access_count
            self.access_count+=1
            return self.values[self.keys.index(key)]
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            if len(self.keys) == self.capacity:
                idx = self.access.index(min(self.access))
                self.keys.pop(idx)
                self.values.pop(idx)
                self.access.pop(idx)
            self.keys.append(key)
            self.values.append(value)
            self.access.append(self.access_count)
            
        else:
            self.values[self.keys.index(key)] = value
            self.access[self.keys.index(key)] = self.access_count
        self.access_count+=1    
