#!/opt/homebrew/bin/python3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head:ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        # Here, we know the size of the list is at least 2
        # head will ALWAYS need to be recalculated. 
        # Let's do that, then tend to the rest of the linked-list
        # we save a reference to head.next
        # the idea is to get head to reference head.next.next,
        # and head.next to reference head.
        # Then we can set head.next as the new head.
        head_next_temp = head.next
        head.next = head.next.next
        head_next_temp.next = head
        head = head_next_temp

        iter_prev = head.next

        # rest of list is similar, 
        # but we need don't need to change head reference.
        # also, we need a reference to the elem before swap (head.next)
        # to be able to assign head.next to the new element in front of it (iter.next)
        # save iter.next into iter_next_temp
        # iter.next = iter.next.next
        # head.next = iter_next_temp

        iter = head.next.next
        while iter is not None and iter.next is not None:
            iter_next_temp = iter.next
            iter.next = iter.next.next
            iter_prev.next = iter_next_temp
            iter_next_temp.next = iter
            iter = iter.next
        return head

def iterate_list(head:ListNode):
    iter = head
    while iter is not None:
        print(iter.val)
        iter = iter.next

head = ListNode()
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
        
print("I made it here")
iterate_list(head)
head = Solution().swapPairs(head)
iterate_list(head)
