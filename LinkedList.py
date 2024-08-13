class Node:
    def __init__(self,itemName,price):
        self.next = None
        self.itemName = itemName
        self.price=price
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def insertAtBeginning(self,itemName,price):
        new_node = Node(itemName,price)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
 
    def insertAtEnd(self,itemName,price):
        new_node = Node(itemName,price)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while(curr_node.next):
            curr_node = curr_node.next
        curr_node.next = new_node
 
    def traverse(self):
        curr_node = self.head
        while(curr_node):
            print(curr_node.itemName)
            print(curr_node.price)
            curr_node = curr_node.next
 
    '''def insertAtMiddle(self,data1,data2):
        new_node = Node(data1)
        curr_node = self.head
        while(curr_node.next):
            if curr_node.data == data2:
                new_node.next = curr_node.next
                curr_node.next = new_node
            curr_node = curr_node.next'''
 
    def search(self, value):
        curr_node = self.head
        position = 0
        while(curr_node):
            if curr_node.itemName == value:
                print(str(value)+" found at position "+str(position))
            curr_node = curr_node.next
            position += 1
        print("Not found")
 
    def deleteFromBeginning(self):
        if self.head is None:
            print("List Empty")
        else:
            self.head= self.head.next
   
    def deleteAtIndex(self, index):
        # If the list is empty, return
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        
        # If the index is 0, delete from the beginning
        if index == 0:
            self.deleteFromBeginning()
            return

        curr_node = self.head
        position = 0
        
        # Traverse to the node just before the one to delete
        while curr_node is not None and position < index - 1:
            curr_node = curr_node.next
            position += 1

        # If curr_node is None, the index is out of bounds
        if curr_node is None or curr_node.next is None:
            print("Index not found")
            return

        # Delete the node at the specified index
        curr_node.next = curr_node.next.next