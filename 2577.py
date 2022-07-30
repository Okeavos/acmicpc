A = int(input())
B = int(input())
C = int(input())

stack = []

k = str(A * B * C)

for u in range(0, 10):
    s = k.count(str(u))
    stack.append(s)

for ll in range(len(stack)):
    print(stack[ll])
