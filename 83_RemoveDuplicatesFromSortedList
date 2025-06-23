# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ## Attempt 1
        # empty = ListNode() 
        # res = empty
        # val = -101
        # current = head
        # while current:
        #     if current.val > val:
        #         res.next = ListNode(current.val)
        #         res = res.next
        #         val = current.val
        #     current = current.next
        # return empty.next

        ##Attempt 2
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
        