a=list(input().upper())
b={}
for char in a:
    if char in b:
        b[char]+=1
    else:
        b[char]=1

max_cnt=max(b.values())
max_chars=[char for char, cnt in b.items() if cnt==max_cnt]

if len(max_chars)>1:
    print('?')
else:
    print(max_chars[0])