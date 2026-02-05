class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return 1 if len(trust) == 0 else -1
        # First, check whether ANYONE is a judge. Easy O(n) check,
        # a judge trusts noone, and everyone trusts the judge,
        # so the outer list must have size at least n - 1
        if len(trust) < n - 1:
            return -1
        judge_index = -1

        # The plan here is to iterate through the whole list once.
        # We should keep track of 2 things:
        # 1. How many nodes have 0 outgoing edges.
        # 2. For each edge, keep track of the node it goes into,
        # and how many edges that node has. If our judge node has
        # n - 1 edges by the end, and we didn't return early from 1,
        # we can return that node at the very end.
        in_count = {i: 0 for i in range(1, n + 1)}
        judge_candidate = [True for _ in range(n)]
        for i in range(0, len(trust) + 1):
            judge_candidate[trust[i][0]] = False
            in_count[trust[i][1]] += 1

        # Next, we have to find the judge index and whether
        # there is more than 1 judge node
        judge_found = False
        judge_index = -1
        for j in range(0, n + 1):
            if judge_candidate[j] and not judge_found:
                judge_found = True
                judge_index = j
            else:
                return -1
        if not judge_found:
            return -1

        # Lastly, we check whether our singular candidate
        # judge has n - 1 edges coming in to it.

        if in_count[judge_index] != n - 1:
            return -1
        return judge_index
