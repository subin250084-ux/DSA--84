class ListADT:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size   # Fixed-size array
        self.length = 0

    # Insert element at the end
    def insert(self, value):
        if self.length == self.size:
            print("List is full")
        else:
            self.arr[self.length] = value
            self.length += 1

    # Insert element at a specific position
    def insert_at(self, pos, value):
        if self.length == self.size:
            print("List is full")
        elif pos < 0 or pos > self.length:
            print("Invalid position")
        else:
            for i in range(self.length, pos, -1):
                self.arr[i] = self.arr[i - 1]
            self.arr[pos] = value
            self.length += 1

    # Delete element at a specific position
    def delete(self, pos):
        if pos < 0 or pos >= self.length:
            print("Invalid position")
        else:
            deleted = self.arr[pos]
            for i in range(pos, self.length - 1):
                self.arr[i] = self.arr[i + 1]
            self.arr[self.length - 1] = None
            self.length -= 1
            return deleted

    # Search for an element
    def search(self, value):
        for i in range(self.length):
            if self.arr[i] == value:
                return i
        return -1

    # Display the list
    def display(self):
        print(self.arr[:self.length])


# Example usage
lst = ListADT(5)

lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.display()          # [10, 20, 30]

lst.insert_at(1, 15)
lst.display()          # [10, 15, 20, 30]

print("Deleted:", lst.delete(2))   # Deleted: 20
lst.display()          # [10, 15, 30]

print("Search 15:", lst.search(15))  # 1
print("Search 50:", lst.search(50))  # -1
