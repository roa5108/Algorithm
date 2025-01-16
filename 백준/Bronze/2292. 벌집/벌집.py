import sys
input=sys.stdin.readline

n=int(input())

box=1
layer=1
while n>box:
    box+=6*layer
    layer+=1
print(layer)