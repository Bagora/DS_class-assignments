class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    result = dummy
    carry = 0

    # Get the values from the current nodes of l1 and l2 (or 0 if the nodes are None)
    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        # Calculate the sum and the carry
        _sum = x + y + carry

        carry = _sum // 10

        # Create a new node with the sum and update the result linked list
        result.next = ListNode(_sum % 10)

        # Move to the next nodes in l1 and l2
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

        result = result.next

    return dummy.next


def buildLinkedList(nums):
    dummy = ListNode()
    current = dummy

    for num in nums:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


def printLinkedList(head):
    current = head
    result = []

    while current:
        result.append(str(current.val))
        current = current.next

    print(' -> '.join(result))


# Test example 1
l1 = buildLinkedList([2, 4, 3])
l2 = buildLinkedList([5, 6, 4])
result = addTwoNumbers(l1, l2)
print("Example 1:")
print("Input:")
printLinkedList(l1)
printLinkedList(l2)
print("Output:")
printLinkedList(result)

# Test example 2
l1 = buildLinkedList([0])
l2 = buildLinkedList([0])
result = addTwoNumbers(l1, l2)
print("Example 2:")
print("Input:")
printLinkedList(l1)
printLinkedList(l2)
print("Output:")
printLinkedList(result)

# Test example 3
l1 = buildLinkedList([9, 9, 9, 9, 9, 9, 9])
l2 = buildLinkedList([9, 9, 9, 9])
result = addTwoNumbers(l1, l2)
print("Example 3:")
print("Input:")
printLinkedList(l1)
printLinkedList(l2)
print("Output:")
printLinkedList(result)
