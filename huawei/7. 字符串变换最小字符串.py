"""
给定一个字符串 s, 最多只能进行一次变换, 返回变换后能得到的最小字符串(按照字典序进行比较)。 变换规则: 交换字符串中任意两个不同位置的字符。

输入描述: 

- 一串小写字母组成的字符串s。

输出描述: 

- 按照要求进行变换得到的最小字符串。

备注: 

- s是都是小写字符组成
- 1<=s.length<=1000

### 示例

> 输入: abcdef
> 
> 
> 输出: abcdef
> 
> 说明: abcdef已经是最小字符串, 不需要交换
> 
> 输入: bcdefa
> 
> 输出: acdefb
> 
> 说明: a和b进行位置交换, 可以得到最小字符串
"""

s = list(input())

res = ["".join(s)]
for i in range(len(s)-1):
    for j in range(i+1, len(s)):
        temp_s = s.copy()
        temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
        res.append("".join(temp_s))

res = sorted(res)

print(res[0])

