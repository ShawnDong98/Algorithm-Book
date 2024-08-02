"""
给定一段密文字符串s, 其中字符都是经过密码本映射的, 现需要将密文解密并且输出。映射的规则 a-i 分别用 1-9 表示; j-z 分别用 10*-26* 表示。约束：映射始终唯一。

示例1
输入：
20*19*20*

输出：
tst

说明：
翻译后的文本长度在 100 以内。
"""
inp = input()

hash_map = {i+1:chr(s) for i, s in enumerate(range(ord("a"), ord("z")))}

i = len(inp) - 1

res = []
while i > -1:
    if inp[i] == "*":
        num = int(inp[i-2:i])
        res.append(hash_map[num])
        i -= 3
    else:
        num = int(inp[i])
        res.append(hash_map[num])
        i -= 1

print("".join(res[::-1]))























































        

    