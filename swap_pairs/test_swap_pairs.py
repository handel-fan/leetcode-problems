import unittest
import swap_pairs


class SwapPairsTests:

    def base_test(self, head:swap_pairs.ListNode, expected_head:swap_pairs.ListNode):

        if head is None and expected_head is None:
            return True

        while head.next is not None and expected_head.next is not None:
            if head is None or expected_head is None:
                return False
            if head.val != expected_head.val:
                return False
            head = head.next
            expected_head = expected_head.next

        if head is None or expected_head is None:
            return False
        if head.next is None or expected_head.next is None:
            return False
        if head.val != expected_head.val:
            return False
        return True




