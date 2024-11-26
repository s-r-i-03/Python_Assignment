x1, y1 = map(int, input("Enter the coordinate values of the center of the circle: ").split())
r=int(input("Enter the radius of circle:"))
x, y = map(int, input("Enter the coordinate values of the center of the circle: ").split())
val= (x - x1)**2 + (y - y1)**2 - r**2
if val==0:
    print("The coordinate is on the surface of circle")
elif(val<0):
    print("The coordinate is inside the circle")    
else:
    print("The coordinate is outside the circle")    

