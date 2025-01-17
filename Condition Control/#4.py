year=int(input("Enter year:"))
days=(year-1900)*365+(year-1900)//4
day_of_week= days%7
if day_of_week==days%7:
    print("Monday")
elif day_of_week==1:
    print("Tuesday")
elif day_of_week==2:
    print("Wednesday")
elif day_of_week==3:
    print("Thrusday")
elif day_of_week==4:
    print("Friday")
elif day_of_week==5:
    print("Saturday")    
else:
    print("Sunday")            

