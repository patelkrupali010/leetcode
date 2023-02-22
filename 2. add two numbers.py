# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            result = ListNode()
            ptr = result # the current node of the result list during loop
            carry = 0
            while l1 or l2 or carry:  # if l1 or l2 is not None or carry is not zero. if carry still nonzero after both list has ended, the loop will continue to add the remaining to digits to result List
                if l1:
                    carry += l1.val
                    l1 = l1.next
                if l2:
                    carry += l2.val
                    l2 = l2.next

                ptr.next = ListNode(carry%10)  # if  sum is greater than 9, only add the last digit to the list and carry the remaining part to next loop
                ptr = ptr.next
                carry //= 10

            return result.next
    