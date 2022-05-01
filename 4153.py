'''while True:
    x, y, z = map(int, input().split())
    
    if x==0 and y == 0 and z == 0 : 
        break
    
    else:
        if (x**2 + y**2) == (z**2):
            print("right")
        else:
            print("wrong")
   '''
# 틀린 이유 : z를 무조건 빗변이라고 생각하고 변수를 두었음.
# 조건 -> x y z 중 가장 큰 수가 빗변이 되어야 함. x**2 + y**2 = z**2
cnt = 0
while True:
    k = list(map(int, input().split()))
    
    for u in range(len(k)): # breaking points
        if k[u] == 0:
            cnt += 1
            ##print("[!] cnt check ok")
    if cnt == 3: 
        ##print("[!] breaking...")
        break
    
    z = max(k)
    
    del k[k.index(z)]
    
    if k[0]**2 + k[1]**2 == z**2:
        print("right")
    else:
        print("wrong")
    
