paint = int(input())
wall = 0
while True:
  a = int(input())
  b = int(input())
  if a * b > paint:
    break
  wall += 1
  paint -= a*b
print(wall)