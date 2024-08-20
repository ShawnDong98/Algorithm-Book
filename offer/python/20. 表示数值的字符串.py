"""
题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

例如, 字符串“+100”、“5e2”、“-123”、“3.1416”及“-1E-16”都表示数值, 但“12e”、“1a3.14”、“1.2.3”、“+-5”及“12e+5.4”都不是。
"""

import re

def is_number(s):
    pattern  = re.compile("^[+-]?(\d+(\.\d*)?|(\,\d+))([eE][+-]?\d+)?$")

    s = s.strip()

    match = pattern.match(s)

    return match is not None


# Test cases
test_cases = ["+100", "5e2", "-123", "3.1416", "-1E-16", "12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]

for test in test_cases:
    print(f"{test}: {is_number(test)}")
