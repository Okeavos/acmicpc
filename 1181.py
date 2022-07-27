n = int(input())

st = []

for _ in range(n):
    st.append(input())

renew_list = set(st) # 중복 값 제거
st = list(renew_list)
st.sort() # 문자열 정렬
st.sort(key = len) # 길이순 정렬

for u in st:
    print(u)
