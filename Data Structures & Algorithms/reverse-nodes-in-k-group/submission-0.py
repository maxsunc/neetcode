# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def printNode(node):
            res = ""
            while node:
                res += str(node.val)
                node = node.next
            print(res)
        def reverseFirstKInPlace(node, startNode):
            counter = 0
            cur = node
            endNode = None
            while k > counter and cur:
                cur = cur.next
                counter += 1
            if not cur and k > counter:
                # didnt get to the end so we will not reverse at all
                return
            endNode = cur # if cur is None thats fine we just don't have an ending we need to care about
            cur = node
            prev = endNode
            counter = 0
            # reverse the nodes
            while k > counter and cur:
                oldNext = cur.next

                cur.next = prev

                prev = cur
                cur = oldNext
                counter += 1
            # point the startinNode to new head (prev)
            if startNode:
                startNode.next = prev
            # point the starting to the new head
            return prev # the new head
            # 
        # reverse every k elements
        counter = 0
        cur = head
        prev = ListNode()
        dummyNode = prev
        while cur:
            if counter % k == 0:
                print(f"calling on {cur.val}")
                # reverse at this poisiton
                
                newHead = reverseFirstKInPlace(cur,prev)
                printNode(prev)
                cur = newHead
            
            prev = cur
            if cur:
                cur = cur.next
            counter += 1

        return dummyNode.next
        


        # [1,2,3,4,5,6]

        # [3,2,1,6,5,4]