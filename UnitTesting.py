import unittest
from LinkedList import LinkedList  # Adjust the import according to your file structure

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        """Set up a new linked list for each test."""
        self.linked_list = LinkedList()
    
    def test_insert_at_beginning_empty_list(self):
        """Test inserting into an empty list."""
        self.linked_list.insertAtBeginning("Item1", 10.0)
        self.assertEqual(self.linked_list.head.itemName, "Item1")
        self.assertEqual(self.linked_list.head.price, 10.0)

    def test_insert_at_beginning_non_empty_list(self):
        """Test inserting at the beginning of a non-empty list."""
        self.linked_list.insertAtBeginning("Item1", 10.0)
        self.linked_list.insertAtBeginning("Item2", 20.0)
        self.assertEqual(self.linked_list.head.itemName, "Item2")
        self.assertEqual(self.linked_list.head.next.itemName, "Item1")
        
    def test_insert_at_end_empty_list(self):
        """Test inserting at the end of an empty list."""
        self.linked_list.insertAtEnd("Item1", 10.0)
        self.assertEqual(self.linked_list.head.itemName, "Item1")
        self.assertEqual(self.linked_list.head.price, 10.0)

    def test_insert_at_end_non_empty_list(self):
        """Test inserting at the end of a non-empty list."""
        self.linked_list.insertAtEnd("Item1", 10.0)
        self.linked_list.insertAtEnd("Item2", 20.0)
        self.assertEqual(self.linked_list.head.next.itemName, "Item2")

    def test_traverse(self):
        """Test the traversal of the linked list."""
        self.linked_list.insertAtBeginning("Item1", 10.0)
        self.linked_list.insertAtEnd("Item2", 20.0)
        self.linked_list.insertAtEnd("Item3", 30.0)

        output = []
        curr_node = self.linked_list.head
        while curr_node:
            output.append((curr_node.itemName, curr_node.price))
            curr_node = curr_node.next
        
        expected_output = [
            ("Item1", 10.0),
            ("Item2", 20.0),
            ("Item3", 30.0),
        ]
        self.assertEqual(output, expected_output)

    def test_search_item_found(self):
        """Test searching for an item that exists."""
        self.linked_list.insertAtBeginning("Item1", 10.0)
        self.linked_list.insertAtEnd("Item2", 20.0)
        
        with self.assertLogs(level='INFO') as log:
            self.linked_list.search("Item2")
            self.assertIn("Item2 found at position 1", log.output)

    def test_search_item_not_found(self):
        """Test searching for an item that does not exist."""
        self.linked_list.insertAtBeginning("Item1", 10.0)
        
        with self.assertLogs(level='INFO') as log:
            self.linked_list.search("Item2")
            self.assertIn("Not found", log.output)

    def test_delete_from_beginning(self):
        """Test deleting from the beginning of the list."""
        self.linked_list.insertAtBeginning("Item1", 10.0)
        self.linked_list.insertAtBeginning("Item2", 20.0)
        self.linked_list.deleteFromBeginning()
        self.assertEqual(self.linked_list.head.itemName, "Item1")

    def test_delete_at_index(self):
        """Test deleting at a specific index."""
        self.linked_list.insertAtBeginning("Item1", 10.0)
        self.linked_list.insertAtEnd("Item2", 20.0)
        self.linked_list.insertAtEnd("Item3", 30.0)
        self.linked_list.deleteAtIndex(1)  # Deleting "Item2"
        
        output = []
        curr_node = self.linked_list.head
        while curr_node:
            output.append(curr_node.itemName)
            curr_node = curr_node.next
        
        expected_output = ["Item1", "Item3"]
        self.assertEqual(output, expected_output)

    def test_delete_at_index_invalid(self):
        """Test deleting at an invalid index."""
        self.linked_list.insertAtBeginning("Item1", 10.0)
        
        with self.assertLogs(level='INFO') as log:
            self.linked_list.deleteAtIndex(1)  # Trying to delete non-existent index
            self.assertIn("Index not found", log.output)

    def test_delete_from_empty_list(self):
        """Test deleting from an empty list."""
        with self.assertLogs(level='INFO') as log:
            self.linked_list.deleteFromBeginning()
            self.assertIn("List Empty", log.output)

if __name__ == '__main__':
    unittest.main()