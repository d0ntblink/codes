def prime_checker(number) :
  isprime = False
  for n in range(2,number - 1) :
    if number % n == 0 :
      isprime = True
      break
    else :
      pass
  if isprime :
    print("It's not a prime number.")
  else :
    print("It's a prime number.")

while True :
    try :
        n = int(input("Check this number: "))
        prime_checker(number=n)
    except :
        print("not a number")