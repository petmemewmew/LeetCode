class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if numRows == 1:
			return s
		ans = ""
		index = 0
		for i in range(numRows):
			if i == 0 or i == numRows - 1:
				while index < len(s):
					ans += s[index]
					index += 2 * numRows - 2
				index = 1
			else:
				while index < len(s):
					ans += s[index]
					index += 2 * numRows - 2 * i -2
					if index < len(s):
						ans += s[index]
						index += 2 * i
				index = i + 1
		return ans