from LinkedList import LinkedList

def test_linked_list():
    
    ll = LinkedList()

    ll.insertAtBeginning("Apple",10)
    ll.insertAtBeginning("Orange",40)
    ll.insertAtBeginning("Pineapple", 50)

    assert ll.head.itemName == "Pineapple", "Test Case 1 Failed"
    assert ll.head.next.itemName == "Orange", "Test Case 2 Failed"
    assert ll.head.next.next.itemName == "Apple", "Test Case 3 Failed"

if __name__ == "__main__":
    test_linked_list()