class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        node = self
        str = ''
        while node is not None:
            str += '%s' % node.val
            node = node.next
        return str

def makeNodeList(li):
    first = True
    for val in li:
        node = ListNode(val)
        if first: 
            first = False
            result = node
            resultCursor = result
        else:
            resultCursor.next = node
            resultCursor = node

    return result

def addTwoNumbers(l1, l2):
    '''
    You are given two linked lists representing two non-negative numbers. 
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8

    >>> print addTwoNumbers(makeNodeList([2,4,3]), makeNodeList([5,6,4]))
    708
    >>> print addTwoNumbers(makeNodeList([2]), makeNodeList([5,6,4]))
    764
    >>> print addTwoNumbers(makeNodeList([9,9,9]), makeNodeList([2]))
    1001
    '''
    def decimalDigits(num):
        return num%10, num/10 

    def addTwoNumbersHelper(node1, node2, carry):
        if node1 == node2 == None:
            if carry == 0:
                return True, None, 0
            return True, ListNode(carry), 0
        d1 = d2 = 0
        if node1 is not None:
            d1 = node1.val
        if node2 is not None:
            d2 = node2.val
        low, high = decimalDigits(d1+d2+carry)

        return False, ListNode(low), high

    l1Cursor = l1
    l2Cursor = l2
    carry = 0
    first = True
    while True:
        ok, node, carry = addTwoNumbersHelper(l1Cursor, l2Cursor, carry)
        if first:
            first = False
            result = node
            resultCursor = result
        if ok:
            if carry != 0: node.next = ListNode(carry)
            resultCursor.next = node
            return result
        if l1Cursor is not None:
            l1Cursor = l1Cursor.next
        if l2Cursor is not None:
            l2Cursor = l2Cursor.next
        resultCursor.next = node
        resultCursor = node

if __name__ == '__main__':
    import doctest
    doctest.testmod()
