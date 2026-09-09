# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        nodes = []

        curr = dummy

        while curr:
            nodes.append(curr)
            curr = curr.next

        # Node before the target
        prev = nodes[-n - 1]

        prev.next = prev.next.next

        return dummy.next

        