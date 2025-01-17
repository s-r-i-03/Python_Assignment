for i in range(10):  # Loop runs 10 times

    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the annual rate of interest (in percentage, e.g., 5 for 5%): ")) / 100  # Convert to decimal
    n = float(input("Enter the number of times interest compounds per year: "))
    t = float(input("Enter the number of years: "))
    a = p * (1 + r / n) ** (n * t)
    print(f" the amount will be: {a:.2f}")
