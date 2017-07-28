# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # fast pointer will outrun slow at twice the speed of the slow
        # pointer (2 steps vs 1 step).
        # Time complexity = O(n + k) = O(n)
        # Space complexity = O(1)
        slow = head
        fast = head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False