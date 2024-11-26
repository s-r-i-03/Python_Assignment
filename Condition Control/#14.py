days=int(input("How many days is the member late?:"))
if days<=5:
    print("The member has to pay fine of 50 paise")
elif days>=6 and days<=10:
    print("The member has to pay fine of Rs. 1")
elif days>10 and days<30:
    print("The member has to pay fine of Rs. 5")
elif days>=30:
    print("Membership Cancelled")        
