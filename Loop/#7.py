positive = negative = zeros = 0
while True:
    num = int(input("Enter a number (or type -999 to stop): "))
    if num == -999:
        break
    elif num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zeros += 1
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zeros)
