# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
	def addTwoDigit(self, l1, l2, carry):
		ans = l1.val + l2.val + carry
		return ans / 10, ans % 10

	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		ret = ListNode()
		ptr = ret
		carry = 0
		while l1 and l2:
			ptr.next = ListNode()
			ptr = ptr.next
			ans = l1.val + l2.val + carry
			carry, ptr.val = ans // 10, ans % 10
			l1 = l1.next
			l2 = l2.next
		while l1:
			ptr.next = ListNode()
			ptr = ptr.next
			ans = l1.val + carry
			carry, ptr.val = ans // 10, ans % 10
			l1 = l1.next

		while l2:
			ptr.next = ListNode()
			ptr = ptr.next
			ans = l2.val + carry
			carry, ptr.val = ans // 10, ans % 10
			l2 = l2.next

		if carry:
			ptr.next = ListNode(val=carry)
		return ret.next