dig = int(input("Enter a five-digit number: "))
sum = 0

while dig >0:
    rem = dig % 10  
    sum = sum + rem  
    dig = dig // 10  

print("The sum of digits is:", sum)
