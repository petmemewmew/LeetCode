class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		flag = 1
		if x < 0:
			flag = -1
		x *= flag
		ans = 0
		digit = 1
		while x:
			ans *= 10
			i = x % 10
			ans += digit * i
			x //= 10
		if ans > 2 ** 31 - 1:
			return 0
		return ans * flag
