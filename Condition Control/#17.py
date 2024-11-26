
time = float(input("Enter the time taken by the worker (in hours): "))
if 2 <= time <= 3:
    print("The worker is highly efficient.")
elif 3 < time <= 4:
    print("The worker is ordered to improve speed.")
elif 4 < time <= 5:
    print("The worker is given training to improve speed.")
elif time> 5:
    print("The worker has to leave the company.")
else:
    print("Invalid input. Time taken must be at least 2 hours.")
