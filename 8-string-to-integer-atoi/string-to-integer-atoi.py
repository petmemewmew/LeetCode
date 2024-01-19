class Solution(object):
	def myAtoi(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0
		while s and s[0] == ' ':
			s = s[1:]
		sign = 1
		if not s:
			return 0
		if s[0] == '-':
			sign = -1
		if s[0] == '-' or s[0] == '+':
			s = s[1:]
		ans = 0
		if not s:
			return 0
		while s and s[0] == 0:
			s = s[1:]
		while s and not ((sign == 1 and ans > 2 ** 31 - 1) or (sign == -1 and ans > 2 ** 31)):
			if s[0] == '0':
				ans *= 10
			elif s[0] == '1':
				ans *= 10
				ans += 1
			elif s[0] == '2':
				ans *= 10
				ans += 2
			elif s[0] == '3':
				ans *= 10
				ans += 3
			elif s[0] == '4':
				ans *= 10
				ans += 4
			elif s[0] == '5':
				ans *= 10
				ans += 5
			elif s[0] == '6':
				ans *= 10
				ans += 6
			elif s[0] == '7':
				ans *= 10
				ans += 7
			elif s[0] == '8':
				ans *= 10
				ans += 8
			elif s[0] == '9':
				ans *= 10
				ans += 9
			else:
				return ans * sign
			s = s[1:]
		if not s and not ((sign == 1 and ans > 2 ** 31 - 1) or (sign == -1 and ans > 2 ** 31)):
			return ans * sign
		if sign == 1:
			return 2 ** 31 - 1
		else:
			return -2 ** 31
