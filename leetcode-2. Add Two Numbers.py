class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

def num_to_listnode(num):
    head = ListNode(num % 10)
    num //= 10
    current = head
    while num > 0:
        current.next = ListNode(num % 10)
        current = current.next
        num //= 10
    return head

def listnode_to_num(node):
    num = 0
    place = 1
    while node:
        num += node.val * place
        place *= 10
        node = node.next
    return num

num1 = int(input())
num2 = int(input())

l1 = num_to_listnode(num1)
l2 = num_to_listnode(num2)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

result_num = listnode_to_num(result)
print(result_num)
