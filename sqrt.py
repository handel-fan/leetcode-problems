class Solution:
    def NaiveMySqrt(self, x: int) -> int:
        if x < 0:
            raise Exception("This algorithm is only for nonnegative numbers")
        if x == 0:
            return 0
        if x < 4:
            return 1
        # We just skipped the need to check x <= 3
        # x can be 4, so natural selection of sqrt(x) to start checking is sqrt(x) = 2

        # The upper bound is 2^31 - 1
        # upper bound for sqrt is 2^30
        i = 2

        # We can return i, if i**2 <= x <= (i + 1)**2

        while i * i < x:
            i += 1

        if i * i == x:
            return i

        return i - 1

    def BinSrchMySqrt(self, x: int) -> int:
        # UNFINISHED
        # Let initial guess be x/2
        i = x / 2
        if i**i == x:
            return i

        return 0


sol = Solution()

test_cases = {
    4: 2,
    8: 2,
    9: 3,
    12: 3,
}

for test_input, expected_value in test_cases.items():
    if sol.NaiveMySqrt(test_input) != expected_value:
        print("failed test case")
        exit(1)
    else:
        print("passed test case")
