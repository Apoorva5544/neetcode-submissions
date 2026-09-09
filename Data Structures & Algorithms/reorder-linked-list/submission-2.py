# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        
        second_list = slow.next
        slow.next = None 
        prev = None 

        while second_list:
            next_node = second_list.next
            second_list.next = prev
            prev = second_list
            second_list = next_node

        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1 
            second = temp2