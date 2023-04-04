a = input()
if len(a) == 4:
 b = a[:2]
 c = a[2:]
 print(b + "I" + c)
else:
  print(a[:1] + "I" + a[1:])