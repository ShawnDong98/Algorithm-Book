"""
已知火星人使用的运算符为 #、$, 其与地球人的等价公式如下：
x#y = 4x+3y+2
x$y = 2*x+y+3
1、其中 x、y 是无符号整数
2、地球人公式按 C 语言规则计算
3、火星人公式中, # 的优先级高于 $, 相同的运算符, 按从左到右的顺序计算
现有一段火星人的字符串报文, 请你来翻译并计算结果。

输入描述

火星人字符串表达式（结尾不带回车换行）

输入的字符串说明： 字符串为仅由无符号整数和操作符（#、$）组成的计算表达式。例如：

`123#4$5#67$78`

1. 用例保证操作数取值范围为32位无符号整数。
2. 保证输入以及计算结果不会出现整型溢出。
3. 保证输入的字符串为合法的求值报文，例如：`123#4$5#67$78`
4. 保证不会出现非法的求值报文，例如类似这样字符串：
    #4$5 //缺少操作数
    4$5# //缺少操作数
    4#$5 //缺少操作数
    4 $5 //有空格
    3+4-5*6/7 //有其它操作符
    12345678987654321$54321 //32位整数计算溢出
    
输出描述

根据输入的火星人字符串输出计算结果（结尾不带回车换行）

用例

输入

7#6$5#12

输出

157
"""

def mars_calculator(num1, num2, op):
    if op == "#":
        return 4 * num1 + 3 * num2 + 2
    else:
        return 2 * num1 + num2 + 3

inp = input()

ops = []
nums = []

i = 0
while i < len(inp):
    if inp[i].isdigit():
        num = []
        while i < len(inp) and inp[i].isdigit():
            num.append(inp[i])
            i += 1

        nums.append(int("".join(num)))
    elif inp[i] in "$#":
        # 当遇到 $ 的时候，已经把 # 计算掉了
        while ops and ops[-1] == "#":
            num2 = nums.pop()
            num1 = nums.pop()
            op = ops.pop()
            nums.append(mars_calculator(num1, num2, op))

        ops.append(inp[i])
        i += 1
    
while ops:
    num2 = nums.pop()
    num1 = nums.pop()
    op = ops.pop()
    nums.append(mars_calculator(num1, num2, op))

print(nums[0])
