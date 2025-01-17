
machine_cost = 6000
annual_earnings = 1000
salvage_value = 2000
rate_of_return = 12  

y = 1

while True:

    business = y * annual_earnings + salvage_value
    investment = (machine_cost * y * rate_of_return) / 100 + machine_cost

    
    if business > investment:
        print("Minimum year =", y)
        break 


    y += 1
