valid = False
while not valid:
  code = input()
  if len((code)) == 5 and code[0:2] == "TH" and code[2:].isdigit():
    valid = True
print(code)
