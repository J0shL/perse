quant = int(input())
curren = input()
if curren == "dobbles":
  print(quant // 2)
elif curren == "dabbles":
  print(quant // 3)
else:
  if input() == "dobbles":
    print(quant *2)
  else:
    print(quant *3)