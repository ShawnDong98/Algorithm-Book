import copy
from typing import List

class Solution:
    """
    2345678
    state = {""}
    for 每个数字
        for c = 当前数字的所有备选字母
            for s = state 中的所有字符串
                s += c
                将 s 加入到新的集合中
    23
    state = {""}
    for 2:
        for a, b, c:
            for "":
                "a", "b", "c"

    state1 = {"a", "b", "c"}
    for 3:
        for d, e, f:
            for "a", "b", "c":
                "ad", "bd", "cd", "ae", "be", "ce", "af", "bf", "cf"
    state2 = {"ad", "bd", "cd", "ae", "be", "ce", "af", "bf", "cf"}
    """
    def letterCombinations_iterative(self, digits: str) -> List[str]:
        if len(digits) == 0: return []

        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        state = ['']
        for digit in digits:
            new_state = []
            for c in phone[digit]:
                for s in state:
                    s += c
                    new_state.append(s)
            state = new_state

        return state


    def letterCombinations_recursive(self, digits: str) -> List[str]:
        if len(digits) == 0: return []

        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(conbination, next_digits):
            if len(next_digits) == 0:
                res.append(conbination)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(conbination + letter, next_digits[1:])

        res = []
        backtrack("", digits)
        return res

digits = "23"
S = Solution()
print(S.letterCombinations_iterative(digits))
