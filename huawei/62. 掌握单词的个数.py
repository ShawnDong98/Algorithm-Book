"""
有一个字符串数组words和一个字符串chars。假如可以用chars中的字母拼写出words中的某个单词(字符串), 那么我们就认为你掌握了这个单词。words的字符仅由 a-z 英文小写字母组成。例如: abc。chars由 a-z 英文小写字母和问号组成。其中英文问号表示万能字符, 能够在拼写时当做任意一个英文字母。例如："?" 可以当做 "a"等字母。注意：每次拼写时, chars中的每个字母和万能字符都只能使用一次。输出词汇表words中你掌握的所有单词的个数。没有掌握任何单词, 则输出0。

输入描述
第一行: 输入数组 words 的个数, 记作N。

第二行~第N+1行: 依次输入数组words的每个字符串元素。

第N+2行: 输入字符串 chars

输出描述
输出一个整数, 表示词汇表 words 中你掌握的单词个数

备注

1 <= words.length <= 100

1 <= words[i].length, chars.length <= 100

所有字符串中都仅包含小写英文字母、英文问号

示例1
输入
4
cat
bt
hat
tree
atach??

输出
3

说明:可以掌握的单词 "cat”、“bt"和"hat"。
示例2
输入
3
hello
world
cloud
welldonehohneyr

输出：
2

说明:可以掌握的单词 "hello”、“world"。

示例3
输入
3
apple
car
window
welldoneapplec?

输出：
2

说明:可以掌握的单词 "apple”、“car"。
"""

N = int(input())

words = []

for i in range(N):
    words.append(input())

chars = input()
magic = chars.count('?')

cnt = 0
for word in words:
    patience = 0
    for s in word:
        if s not in chars:
            patience += 1
    if patience > magic:
        break
    cnt += 1

print(cnt)
