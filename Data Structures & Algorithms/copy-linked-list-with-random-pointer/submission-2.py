class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        original = []
        curr = head

        # Store original nodes
        while curr:
            original.append(curr)
            curr = curr.next

        # Create copied nodes
        copied = [Node(node.val) for node in original]

        # Map original node -> index
        index = {}
        for i in range(len(original)):
            index[original[i]] = i

        # Connect pointers
        for i in range(len(original)):
            if i + 1 < len(copied):
                copied[i].next = copied[i + 1]

            if original[i].random:
                copied[i].random = copied[index[original[i].random]]

        return copied[0]


