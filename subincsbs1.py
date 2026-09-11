class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Delete a node
    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        # If the first node contains the data
        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Element not found")

    # Search for an element
    def search(self, data):
        temp = self.head

        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next

        return False

    # Display the list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
L = SinglyLinkedList()

L.insert_end(10)
L.insert_end(20)
L.insert_end(30)

print("Linked List:")
L.display()

L.insert_beginning(5)
print("After inserting 5 at beginning:")
L.display()

L.delete(20)
print("After deleting 20:")
L.display()

print("Search 30:", L.search(30))

