# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy

        while True:
            c =self.getK(groupPrev,k)
            if not c:
                break
            gnext = c.next

            prev = c.next
            curr = groupPrev.next

            while curr!=gnext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            
            groupPrev.next = c
            groupPrev = tmp

        return dummy.next

    def getK(self, curr,k):
        while curr and k>0:
            curr = curr.next;
            # print(curr.val)
            k-=1;

        return curr;