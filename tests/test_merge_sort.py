import os
import sys
sys.path.insert(0, '..')

#print("cwd: ", os.getcwd())
#print("..", os.listdir('../..'))
#print("path: ", sys.path)
#print(sys.modules.keys());

import unittest
import merge_sort

class TestMergeSort(unittest.TestCase):   
    # This is a method because it is under the scope of the class...?
    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(merge_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3]), [1, 2, 3])

    def test_unsorted_list(self):
        self.assertEqual(merge_sort([2, 1, 7, 9, 5]), [1, 2, 5, 7, 9])

if __name__ == "__main__":
    unittest.main()
