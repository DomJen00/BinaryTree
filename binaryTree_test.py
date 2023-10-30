import unittest
from binaryTree import BinTree

class BinTreeTestMethods(unittest.TestCase):
    def test_should_find_the_first_element(self):
        # Given a binary tree with example data
        exampleData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bt = BinTree(exampleData)

        # When searched for the first element
        result = bt.contains(exampleData[0])

        # Then it should return True
        self.assertTrue(result)

    def test_should_find_the_last_element(self):
        # Given a binary tree with example data
        exampleData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        size = len(exampleData) - 1
        bt = BinTree(exampleData)

        # When searched for the last element
        result = bt.contains(exampleData[size])

        # Then it should return True
        self.assertTrue(result)

    def test_should_find_the_mid_element(self):
        # Given a binary tree with example data
        exampleData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        max_index = len(exampleData) - 1
        min_index = 0
        mid_index = (max_index + min_index) // 2
        bt = BinTree(exampleData)

        # When searched for the mid element
        result = bt.contains(exampleData[mid_index])

        # Then it should return True
        self.assertTrue(result)   

    def test_should_return_false_if_no_element_is_existing(self):
        # Given a binary tree with empty example data
        exampleData = []
        bt = BinTree(exampleData)

        # When searched for a element in empty data list
        result = bt.contains(0)

        # Then it should return False
        self.assertFalse(result)


    def test_should_return_false_if_element_is_not_existing(self):
        # Given a binary tree with example data
        exampleData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bt = BinTree(exampleData)

        # When searched for a element which not exists
        result = bt.contains(11)

        # Then it should return False
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()