class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.count = 0
    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.cache[key] = count
            count+=1
            return self.cache.keys().index(key)
        return -1
    def put(self, key: int, value: int) -> None:
                
