for num in range(1, 501):
    sum_of_cubes = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10
    if num == sum_of_cubes:
        print(num, "is an Armstrong number")
