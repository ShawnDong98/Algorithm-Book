"""
题目： 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。假设字符串中只包含 'a' ~ 'z' 的字符。例如，在字符串 "arabcacfr" 中，最长的不含重复字符的子字符串是 "acfr"，长度为 4。
"""
def func(inp):
    res = []
    for start in range(0, len(inp)-1):
        for end in range(start+1, len(inp)):
            sub_str = inp[start:end]
            if len(set(sub_str)) == len(sub_str):
                res.append(sub_str)

    res = sorted(res, key=lambda x:-len(x))

    return res[0]

inp = "arabcacfr"
print(func(inp))