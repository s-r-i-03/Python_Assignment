health = input("Enter the person's health (excellent/poor): ").lower()
age = int(input("Enter the person's age: "))
location = input("Enter the person's location (city/village): ").lower()
sex = input("Enter the person's sex (male/female): ").lower()
if health == "excellent" and 25 <= age <= 35 and location == "city" and sex == "male":
    premium = 4 
    policy_amount = 200000  
    print(f"The person is insured with a premium rate of Rs. {premium} per thousand.")
    print(f"The maximum amount for which he can be insured is Rs. {policy_amount}.")
    
elif health == "excellent" and 25 <= age <= 35 and location == "city" and sex == "female":
    premium = 3  
    policy_amount = 100000  
    print(f"The person is insured with a premium rate of Rs. {premium} per thousand.")
    print(f"The maximum amount for which she can be insured is Rs. {policy_amount}.")
    
elif health == "poor" and 25 <= age <= 35 and location == "village" and sex == "male":
    premium = 6  
    policy_amount = 10000  
    print(f"The person is insured with a premium rate of Rs. {premium} per thousand.")
    print(f"The maximum amount for which he can be insured is Rs. {policy_amount}.")
    
else:
    print("The person is not insured.")
