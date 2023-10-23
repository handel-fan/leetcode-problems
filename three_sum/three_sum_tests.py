#!/opt/homebrew/bin/python3
import unittest
import three_sum
from typing import List, Tuple

class ThreeSumTests(unittest.TestCase):

    # Some relevant tests:
    # Empty List, 3 0s (standard), 5 0s (check duplicate elements), 
    # negative #s (standard), negs with duplicate elements,
    # size of integers: we have issues. What is int_max + 1? Is this
    # a valid triplet? im, 1, 0
    #
    # Let's look at a few more:
    # multiple correct solns
    # no solns
    # 
    #
    def base_test(
        self, 
        listInput:List[int], 
        expectedTupleList:List[Tuple[int, int, int]]
        ):
        self.assertEqual(
            sorted(three_sum.three_sum(sorted(listInput))), 
            sorted(
                [tuple(sorted(t)) for t in expectedTupleList]
            )
        )

    def test_empty_set(self):
        self.base_test([], [])

    def test_3_0s(self):
        self.base_test([0, 0, 0], [(0, 0, 0)])

    def test_no_solns_3_nums(self):
        self.base_test([1, 2, 3], [])

    def test_no_solns_5_nums(self):
        self.base_test([1, 2, 3, 4], [])

    def test_2_solns(self):
        self.base_test([1, 2, -3, 0, 0, 0], [(1, 2, -3), (0, 0, 0)])

    def test_5_0s(self):
        self.base_test([0, 0, 0, 0, 0], [(0, 0, 0)])

    def test_0s_neg_1_1(self):
        self.base_test([0, 0, 0, -1, 1], [(0, 0, 0), (-1, 0, 1)])

    def test_i_incorrect(self):
        self.base_test([-1, -1, 0, 1, 0, 0], [(0, 0, 0), (-1, 0, 1)])

    def test_int_limits(self):
        lower_limit = -10**5
        upper_limit = 10**5
        self.base_test([lower_limit, upper_limit, 0], [(lower_limit, upper_limit, 0)])
    
    if __name__ == "__main__":
        unittest.main()
