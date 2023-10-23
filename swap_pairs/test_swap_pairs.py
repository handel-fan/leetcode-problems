import unittest
import swap_pairs


class SwapPairsTests:

    def base_test(self, head:swap_pairs.ListNode, expected_head:swap_pairs.ListNode):

        while head is not None and expected_head is not None:
            if head.val != expected_head.val:
                return False
            head = head.next
            expected_head = expected_head.next

        if head is None or expected_head is None:
            return False
        return True




