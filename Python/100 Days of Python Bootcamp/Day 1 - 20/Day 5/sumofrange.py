'''Instructions
You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 2 and 100.

e.g. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Hint
There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.'''

rangenums = input("chose start and and the end of your range and then the steps(1 for all , 2 for even) in order, seperating them with an space : ").split(" ")
rangenums = list(map(int, rangenums))
numtotal = 0
for num in range(rangenums[0], rangenums[1]+1 , rangenums[2]):
    numtotal += num

print(F"total sum of the all the numbers are {numtotal}")