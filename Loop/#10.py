numbers = []
while True:
    num = input("Enter a number: ")
    if num.lower() == 'done':
        break
    numbers.append(int(num))

if numbers:
    range_of_numbers = max(numbers) - min(numbers)
    print("The range of the set of numbers is:", range_of_numbers)
else:
    print("No numbers were entered.")
