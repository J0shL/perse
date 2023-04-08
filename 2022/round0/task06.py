time = int(input())
tick = 0
while time > 0:
  if time > 0:
   print(time - tick)
   time -= tick
   tick += 1
  else:
    print("0")
