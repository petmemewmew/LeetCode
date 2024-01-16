class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if numRows == 1:
			return s
		ans = []
		for i in range(numRows):
			ans.append("")
		index = 0
		direction = 1
		for i in range(len(s)):
			ans[index] += s[i]
			if direction == 1:
				if index != numRows - 1:
					index += 1
				else:
					direction = -1
					index -= 1
			else:
				if index != 0:
					index -= 1
				else:
					direction = 1
					index += 1
		ret = "".join(ans)
		return ret
