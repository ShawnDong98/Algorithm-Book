"""
题目:实现函数 double Power(double base, int exponent)，求 base 的exponent 次方。不得使用库函数，同时不需要考虑大数问题。
"""

def func(base, exponent):
    if base == 0 and exponent == 0:
        return 1
    if base == 0:
        return 0
    if exponent == 0:
        return 1
    
    if exponent < 0:
        base = 1 / base
        exponent = abs(exponent)

    def fast_pow(base, exponent):
        if exponent == 0:
            return 1
        
        half = fast_pow(base, exponent // 2)
        if exponent % 2 == 0:
            return half * half
        else:
            return half * half * base
        
    
    return fast_pow(base, exponent)


base = 2
exponent = -3
print(func(base, exponent))