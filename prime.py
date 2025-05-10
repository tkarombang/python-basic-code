def isPrime(number):
  if number <= 1:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True

def cetakPrime(n):
  for i in range(1, n+1):
    if isPrime(i) == True:
      print(i, "Bilangan Prima")
    else:
      print(i, "BUKAN Bilangan Prima")

cetakPrime(15)