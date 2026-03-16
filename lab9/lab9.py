class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# User Input Program
if __name__ == '__main__':
    ll = LinkedList()
    while True:
        print('\nOptions:')
        print('1. Add at Beginning')
        print('2. Add at End')
        print('3. Display')
        print('4. Search')
        print('5. Delete First')
        print('6. Count')
        print('7. Reverse List')
        print('8. Exit')
        choice = int(input('Enter choice: '))
        if choice == 1:
            data = input('Enter value to add at beginning: ')
            ll.add_at_beginning(data)
        elif choice == 2:
            data = input('Enter value to add at end: ')
            ll.add_at_end(data)
        elif choice == 3:
            ll.display()
        elif choice == 4:
            key = input('Enter value to search: ')
            found = ll.search(key)
            print('Found' if found else 'Not Found')
        elif choice == 5:
            ll.delete_first()
        elif choice == 6:
            print('Count:', ll.count())
        elif choice == 7:
            ll.reverse_list()
            print('List reversed')
        elif choice == 8:
            break
        else:
            print('Invalid choice!')
