#!/opt/homebrew/bin/python3

# naive soln:
# Iterate over list with triple for loop
# In 1st loop, we iterate through n elements
# in 2nd loop, we iterate n - 1 elements (skipping element we've "picked" in 1st loop)
# in 3rd loop, we iterate n - 2 elements
# 
# The idea is to do the following:
# If we have picked this element in a "higher" up loop, skip and move on.
# If not, add to "higher" loop element.
# Do this for all 3 loops, for each elemnet. Each time, check whether the sum was achieved.
#
# Bad for multiple reasons - 
# It is O(n^3)
# n * (n - 1) * (n - 2) = (n^2 - n)(n-2)
# = n^3 + some shit = O(n^3)
#
# First let's improve worst-case runtime
# sorting costs n(log(n))
# 

from typing import List

class Solution(object):
    def three_sum(self, nums: List[int]):
        triplets = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_calc = nums[i] + nums[j] + nums[k] 
                if sum_calc == 0:
                    triplets.append((nums[i], nums[j], nums[k]))
                    # avoid repeat nums[j]
                    j += 1
                    while j < k - 1 and nums[j] == nums[j - 1]: 
                        j += 1
                    # we need to deal with last comparison here; note j < k - 1 stops us short
                    # If we're not at j < k - 1, we're good - comparing again doesn't hurt.
                    if nums[j] == nums[j - 1]:
                        j += 1
                elif sum_calc < 0:
                    j += 1
                else:
                    k -= 1
            # Does work done inside this loop <= n?
            # Note that as soon as we find a triplet, we're on to finishing with i.
            # We never repeat on i + some constant, we ALWAYS move towards k with j
            # And if the element is too big, we ALWAYS move towards j with k

            # We (supposedly) explored all combinations for the current i. Let's 
            # move on to the next unique i to avoid duplicates.
            # Ask chatgpt about this
            #
            while nums[i] == nums[i + 1] and i < len(nums) - 2: 
                i += 1

            # We do 1 more here because previous while loop 
            # would get us at the duplicate element.
            # Ex:
            # a a b c
            # i
            # after while loop:
            # a a b c
            #   i
            # after i += 1
            # a a b c 
            #     i
            i += 1

        return triplets

# Work done is sorting + discovering triplets:
# O(nlogn) + O(n^2) = O(n^2)

# print(three_sum([-1, -1, 0, 1, 0]))

# print(three_sum([1, 0, 0, 0, 0, 0]))
# print(three_sum([1, 2, 3]))
# print(three_sum([-5, 2, 3, 1]))
# print(three_sum([0, 0, -5, 2, 3, 1]))

