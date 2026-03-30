# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # lists = length of k linked lists
        # merge k linkedlists together 
        # O(n * k) solution
        # merge 2 linked lists. to create one list, remove those 2 lists and add back this current list
        # repeat until one element remains
        # 
        def mergeLists(l1, l2):
            res = ListNode()
            head = res
            while l1 and l2:
                if l1.val < l2.val:
                    # merge l1 in
                    res.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    res.next = ListNode(l2.val)
                    l2 = l2.next
                res = res.next
            while l1:
                res.next = ListNode(l1.val)
                l1 = l1.next
                res = res.next
            
            while l2:
                res.next = ListNode(l2.val)
                l2 = l2.next
                res = res.next
            
            return head.next



        while len(lists) > 1:
            # grab the first 2 elements
            l1 = lists.pop()
            l2 = lists.pop()
            merged = mergeLists(l1,l2)
            lists.append(merged)


    

        return lists[0] if lists else None



