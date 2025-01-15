sound=list(map(int,input().split()))

if sound==sorted(sound):
    print('ascending')
elif sound==sorted(sound,reverse=True):
    print('descending')
else:
    print('mixed')