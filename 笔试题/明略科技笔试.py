#coding=utf-8
#coding=utf-8
import sys
x = int(sys.stdin.readline().strip())
y = int(sys.stdin.readline().strip())
if x > y:
    greater = x
else:
    greater = y
while True:
    if (greater % x == 0) and (greater % y == 0):
        resu = greater
        break
    greater += 1
print(resu)












