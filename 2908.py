x, y = map(str, input().split())

rex = int("".join(reversed(x)))
rey = int("".join(reversed(y)))

if rex > rey : print(rex)
elif rex < rey: print(rey)
