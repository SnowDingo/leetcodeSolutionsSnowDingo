# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        list3 = answer
        po1 = list1
        po2 = list2
        # we want the loop to end when both list is reached until the end
        while (po1 != None and po2 != None):
            print(po1)
            print(po2)
            # if po1 is smaller than insert po1 and move po1 to the next
            if(po1.val < po2.val):
                list3.next = po1
                po1 = po1.next
            else:
                list3.next = po2
                po2 = po2.next
            # No matter which side we insert we will move the list 3 node to next node for next insertion
            list3 = list3.next
        # at the end return the original new linked list's next(after 0)
        # and the if statement below assigns the remaining one item to the list depending on which linkedlist is still not empty
        if(po1 != None):
            list3.next = po1
        elif(po2!= None):
            list3.next = po2
        return answer.next