volume = int(input())
change = input()
if change == "UP":
  volume += 1
else:
  volume -= 1
if volume >= 10:
  volume = 10
elif volume < 0:
  volume = 0
print(volume)