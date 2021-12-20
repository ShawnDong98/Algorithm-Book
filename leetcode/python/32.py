class Solution:
    def longestValidParentheses(self, s: str) -> int:
	stack = [-1]
	ret = 0
	lg = len(s)
	for i in range(lg):
	    if s[i] == '(':
		stack.append(i)
	    else:
		stack.pop()
		if not stack:
		    stack.append(i)
		else:
		    ret = max(ret, i - stack[-1])
	return ret
