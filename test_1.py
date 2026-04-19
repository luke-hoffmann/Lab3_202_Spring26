import unittest

from lab3_1 import ArrayList, resize, insert


class TestArrayList(unittest.TestCase):

    def test_resize(self):
        arr1 = ArrayList(4, [10, 20, None, None], 2)
        arr2 = resize(arr1)

        self.assertEqual(arr1.size, 4)
        self.assertEqual(arr1.array, [10, 20, None, None])
        self.assertEqual(arr1.next, 2)

        self.assertEqual(arr2.size, 8)
        self.assertEqual(
            arr2.array,
            [10, 20, None, None, None, None, None, None]
        )
        self.assertEqual(arr2.next, 2)
    def test_insert_without_resize(self):
        arr1 = ArrayList(4, [10, 20, None, None], 2)
        arr2 = insert(arr1, 30)

        self.assertEqual(arr1.size, 4)
        self.assertEqual(arr1.array, [10, 20, None, None])
        self.assertEqual(arr1.next, 2)

        self.assertEqual(arr2.size, 4)
        self.assertEqual(arr2.array, [10, 20, 30, None])
        self.assertEqual(arr2.next, 3)
    def test_insert_with_resize(self):
        arr1 = ArrayList(2, [10, 20], 2)
        arr2 = insert(arr1, 30)

        self.assertEqual(arr1.size, 2)
        self.assertEqual(arr1.array, [10, 20])
        self.assertEqual(arr1.next, 2)

        self.assertEqual(arr2.size, 4)
        self.assertEqual(arr2.array, [10, 20, 30, None])
        self.assertEqual(arr2.next, 3)
    

if __name__ == "__main__":
    unittest.main()