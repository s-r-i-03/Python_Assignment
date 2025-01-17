num = int(input("Enter a number: "))
octal = ""
temp = num
while temp > 0:
    remainder = temp % 8
    octal = str(remainder) + octal
    temp //= 8
print("The octal equivalent of", num, "is", octal)
