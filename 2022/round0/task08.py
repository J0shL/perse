word = input()
stop = 0
b = ""
while stop == 0:
  if word == "stop":
    stop += 1
    print(b)
  else:
   b += word+" "
   word = input()
