class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.set(self.size, n)
        self.size += 1
        

    def popback(self) -> int:
        last_i = self.size - 1
        item = self.arr[last_i]
        self.arr[last_i] = 0
        self.size -= 1
        return item

    def resize(self) -> None:
        new_cap = self.capacity * 2
        new_arr = [0] * new_cap
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_cap

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
