len=float(input("Enter the length of rectangle:"))
bre=float(input("Enter the breadth of rectangle"))
area= len*bre
peri=2*(len+bre)
if area>peri:
    print("area is greater than perimeter")
else:
    print("area is not greater than perimeter")    