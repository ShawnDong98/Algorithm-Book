def eval():
    b = num.pop()
    a = num.pop()
    c = op.pop()
    if c == '+':
        x = a + b
    elif c == '-':
        x = a - b
    elif c == '*':
        x = a * b
    elif c == '/':
        x = int(a / b)
    num.append(x)

pr = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}

digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

num = []
op = []
strs = input().strip()

i = 0
while i < len(strs):
    c = strs[i]
    if c in digits:
        x = 0
        j = i
        while j < len(strs) and strs[j] in digits:
            x = x * 10 + int(strs[j])
            j += 1
        i = j - 1
        num.append(x)
    elif c == '(': op.append(c)
    elif c == ')':
        while op[-1] != '(': eval()
        op.pop()
    else:
        while (len(op) > 0 and op[-1] != '(' and pr[op[-1]] >= pr[c]):
            eval()
        op.append(c)
    i += 1
while len(op): eval()
print(num[-1])


