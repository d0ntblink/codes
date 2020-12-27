'''You are going to write a program that automatically prints the solution to the FizzBuzz game.

Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

`When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
`When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
`And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`'''
rangenums = input("chose start and and the end of your range in order, seperating them with an space : ").split(" ")
rangenums = list(map(int, rangenums))
for num in range(rangenums[0], rangenums[1]+1):
    if num % 3 == 0 and num % 5 != 0 :
        print("Fizz")
    elif num % 5 == 0 and num % 3 != 0 :
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0 :
        print("FizzBuzz")
    else :
        print(num)