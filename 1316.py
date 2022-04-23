N = int(input())
cnt = 0

for _ in range(N):
    s = input()
    ek = 0
    
    for index in range(len(s)-1):
        if s[index] != s[index+1]:
            new_word = s[index+1:]
            if new_word.count(s[index]) > 0:
                ek += 1
    
    if ek == 0:
        cnt += 1

print(cnt)
    
