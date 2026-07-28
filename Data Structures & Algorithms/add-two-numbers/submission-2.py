# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # thoughts
        # - start simple by adding ones only
        # - have a loop thorugh both list
        # - track the tens
        # - add the tens using loop to make sure all numbers added

        # add num 1 and num 2
        head = ListNode()
        curr = head
        tens = False # at most mean add 1

        while True:
            tempSum = l1.val + l2.val
            if tens:
                tempSum += 1
                tens = False
            if tempSum >= 10:  # check if it has "tens"
                ones = tempSum % 10
                curr.val = ones
                tens = True
            else:  # 1 digit + 1 digit produces 1 digit
                curr.val = tempSum
            # advances to the next node
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
                curr.next = ListNode()
                curr = curr.next
            else:
                break

        remainderNode = None
        if l1.next:
            remainderNode = l1.next
            curr.next = remainderNode
            curr = curr.next
        elif l2.next:
            remainderNode = l2.next
            curr.next = remainderNode
            curr = curr.next
        
        # no remainder and still has tens
        if not remainderNode and tens:
            curr.next = ListNode()
            curr.next.val = 1
        elif remainderNode and tens:
            # second iteration to make sure all added
            while True:
                tempSum = curr.val + 1
                if tempSum >= 10:
                    curr.val = 0 # has to be 0
                    tens = True
                else:
                    curr.val = tempSum
                    tens = False
                
                if not tens:
                    break
                elif tens and not curr.next:
                    curr.next = ListNode()
                    curr = curr.next
                elif tens and curr.next:
                    curr = curr.next

        return head


# Time Complexity
# O(n) obvious
# Space Complexity
# O(n) obvious

# TODO:
# Learn this approach
# Definition for singly-linked list.
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         cur = dummy

#         carry = 0
#         while l1 or l2 or carry:
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0

#             # new digit
#             val = v1 + v2 + carry
#             carry = val // 10
#             val = val % 10
#             cur.next = ListNode(val)

#             # update ptrs
#             cur = cur.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None

#         return dummy.next