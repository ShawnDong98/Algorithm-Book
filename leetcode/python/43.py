class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_num1 = 0
        for s in num1:
            int_num1 = int_num1 * 10 + int(s)

        int_num2 = 0
        for s in num2:
            int_num2 = int_num2 * 10 + int(s)

        return str(int_num1 * int_num2)
