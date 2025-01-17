x,y,z=map(int,input("Enter the three sides of triangle:").split())
if (x+y>z) or (x+z>y) or (y+z>x):
    print("Triangle is valid")
else:    
    print("Triangle is not valid")