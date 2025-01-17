import math
sum = 0
for n in range(1, 8):
    term = n / math.factorial(n)
    sum += term

print("The sum of the first seven terms is:", sum)
