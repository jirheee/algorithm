from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        addedNode = ListNode((l1.val + l2.val) % 10)
        if l1.val + l2.val >= 10:
            l1.next = self.addTwoNumbers(l1.next, ListNode(1))
        
        addedNode.next = self.addTwoNumbers(l1.next, l2.next)

        return addedNode
    
def printNode(node: ListNode):
    if node == None:
        print("None")
        return

    vals = []
    while 1:
        vals.append(node.val)
        node = node.next
        if node == None:
            break
    print(", ".join(map(str, vals)))

if __name__ == "__main__":
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    answer = Solution().addTwoNumbers(l1, l2)

    printNode(answer)

    