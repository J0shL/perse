balance = 0
streak = 0
while True:
  rev = int(input())
  balance += rev
  if balance < 0:
    streak += 1
  else:
    streak = 0
  if balance <= -1000 or streak == 3:
    break
print(balance)