a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
list = [a, b, c, d, e]
list.sort()
a = (list[0]-10)*10000
b = (list[1]-20)*1000
c = (list[2]-30)*100
d = (list[3]-40)*10
e = list[4]-50
print(a+b+c+d+e)
