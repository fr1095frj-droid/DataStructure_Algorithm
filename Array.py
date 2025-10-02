class Array:
    def __init__(self, array, count, length):
        self.array = array
        self.count = count
        self.length = length

        if self.count < self.length:
            for i in range(self.length - self.count):
                self.array += ['_']

    def print(self):
        for i in range(self.count):
            print(self.array[i], end=' ')
        print()


    def indexOf(self, item):
        for i in range(self.count):
            if self.array[i] == item:
                return i
        return -1


    def insert(self, item):
        if self.count == self.length:
            self.length *= 2
            new_array = ["_"] * self.length
            for i in range(self.count):
                new_array[i] = self.array[i]
            self.array = new_array
        self.array[self.count] = item
        self.count += 1


    def removeAt(self, index):
        if 0 <= index <= self.count:
            for i in range(index, self.count):
                self.array[i] = self.array[i+1]
            self.count -= 1

