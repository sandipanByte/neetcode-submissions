class Solution:
    def reverseKGroup(self, head, k):

        def reverse(start, end):
            prev = None
            curr = start

            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        dummy = ListNode(0)
        dummy.next = head

        prev_group = dummy
        curr = head

        while curr:
            # Find the kth node
            kth = curr

            for _ in range(k - 1):
                if kth is None:
                    return dummy.next
                kth = kth.next

            # Not enough nodes
            if kth is None:
                break

            next_group = kth.next

            # Reverse current group
            new_head = reverse(curr, next_group)

            # Connect previous group
            prev_group.next = new_head

            # curr is now the last node of the reversed group
            curr.next = next_group

            # Move to next group
            prev_group = curr
            curr = next_group

        return dummy.next
