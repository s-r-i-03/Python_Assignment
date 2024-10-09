num = int(input("Enter a four-digit number: "))
last = num % 10 
while num >= 10:
    num //= 10

print("Sum of the first and last digits is:", num+last)
