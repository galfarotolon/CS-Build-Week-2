# each LL represents a single number in reverse
# add both LLs and return another LL 
# reverse that returned LL to get the actual sum

# O(n) time complexity since traversal through both LLs is 
# needed

# add each curr node from each list
# if addition is more than 9, carry the 1 to the next
# node addition

# check if lists are empty and if carryover is equal to 0



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # create the pointers
        p1 = l1
        p2 = l2
        
        # carry counter
        carry = 0
       
       # declare curr variable to help traverse
       # and add notes to the ll
        head = cur = ListNode(0)
        
        # iterate over pointers and carry
        while p1 or p2 or carry:
            print(p1.val, p2.val, carry)
            
            # set curr value to carry
            currentVal = carry
            # add 1st value to ll1 to 1st value of ll2
            currentVal += 0 if p1 is None else p1.val
            currentVal += 0 if p2 is None else p2.val
            
            # if over 10, subtract 10
            if currentVal >= 10:
                # reset the current val to 0
                currentVal -= 10
                # pass on the carry value
                carry = 1
            else:
                # reset carry after adding ll1 and ll2 for next node
                carry = 0
                
            print(currentVal, carry)
            
            # add curr value as it will always be at least 1
            cur.next = ListNode(currentVal)
            cur = cur.next
            
            # if there are no more digits, exit
            if p1 is None and p2 is None:
                break
            # if one of them is none
            elif p1 is None:
                # base check 
                p2 = p2.next
            elif p2 is None:
                p1 = p1.next
            else:
                # if both are not none, go to the next nodes
                p1 = p1.next
                p2 = p2.next
        
        return head.next