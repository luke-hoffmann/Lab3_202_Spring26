import unittest

from lab3_2 import Node, newhead, append, delete, get, get_length, insert


class TestLinkedList(unittest.TestCase):

    def test_newhead(self):
        lst1 = Node(4, Node(3, Node(2)))
        lst2 = newhead(lst1, 5)

        self.assertEqual(lst1, Node(4, Node(3, Node(2))))
        self.assertEqual(lst2, Node(5, Node(4, Node(3, Node(2)))))

    def test_append(self):
        lst1 = Node(4, Node(3, Node(2)))
        lst2 = append(lst1, 1)

        self.assertEqual(lst1, Node(4, Node(3, Node(2))))
        self.assertEqual(lst2, Node(4, Node(3, Node(2, Node(1)))))

    def test_delete(self):
        lst1 = Node(4, Node(3, Node(2)))
        lst2 = delete(lst1, 1)

        self.assertEqual(lst1, Node(4, Node(3, Node(2))))
        self.assertEqual(lst2, Node(4, Node(2)))

    def test_get(self):
        lst1 = Node(4, Node(3, Node(2)))

        self.assertEqual(get(lst1, 0), 4)
        self.assertEqual(get(lst1, 1), 3)
        self.assertEqual(get(lst1, 2), 2)

    def test_get_length(self):
        lst1 = Node(4, Node(3, Node(2)))

        self.assertEqual(get_length(lst1), 3)
        self.assertEqual(get_length(Node(7)), 1)
        self.assertEqual(get_length(None), 0)

    def test_insert_at_front(self):
        lst1 = Node(4, Node(3, Node(2)))
        lst2 = insert(lst1, 0, 9)

        self.assertEqual(lst1, Node(4, Node(3, Node(2))))
        self.assertEqual(lst2, Node(9, Node(4, Node(3, Node(2)))))

    def test_insert_in_middle(self):
        lst1 = Node(4, Node(3, Node(2)))
        lst2 = insert(lst1, 2, 9)

        self.assertEqual(lst1, Node(4, Node(3, Node(2))))
        self.assertEqual(lst2, Node(4, Node(3, Node(9, Node(2)))))

    def test_insert_at_end(self):
        lst1 = Node(4, Node(3, Node(2)))
        lst2 = insert(lst1, 3, 9)

        self.assertEqual(lst1, Node(4, Node(3, Node(2))))
        self.assertEqual(lst2, Node(4, Node(3, Node(2, Node(9)))))


if __name__ == "__main__":
    unittest.main()