n1 = 1
n2 =2
for i in range(1, 5):
  next = n1 + n2
  if i < 2:
    print(i)
  n1 = n2
  n2 = next
  print(n1)