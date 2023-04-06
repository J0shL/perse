a = input()

if a == "lettuce" or a == "carrot":
  a = 50
  ket = input()
  if ket == "y":
    ket = 1
  else:
    ket = 0
  
if a == "beetroot":
  a = 70
  ket = 0
g = int(input())

print(a + ket*15 + 5*g)
