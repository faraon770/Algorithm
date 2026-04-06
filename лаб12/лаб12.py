# Task 1

def hash_function_example(input):
    # Example of a simple hash function implementation
    return hash(input) % 100

# Task 2

def check_collision(key1, key2):
    return hash_function_example(key1) == hash_function_example(key2)

# Task 3

class HashTable:
    def __init__(self):
        self.table = [None] * 100
    # Task 4
    def insert(self, key, value):
        index = hash_function_example(key)
        self.table[index] = value
    # Task 5
    def get(self, key):
        index = hash_function_example(key)
        return self.table[index]
    # Task 6
    def remove(self, key):
        index = hash_function_example(key)
        self.table[index] = None
    # Task 7
    def display(self):
        for index, value in enumerate(self.table):
            if value is not None:
                print(f'Index: {index}, Value: {value}') 
    # Task 8
    def is_empty(self):
        return all(value is None for value in self.table)
    # Task 9
    def size(self):
        return sum(1 for value in self.table if value is not None)
  
# Task 10

table = HashTable()
table.insert('key1', 'value1')
table.display()