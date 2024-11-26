x,y,z=map(int,input("Enter the three sides of a trinagle").split())

if x != y and y != z and x != z:
    print("Triangle is Scalene")
elif x==y==z:
    print("Triangle is Equilateral")
elif x==y or y==z or x==z:
    print("Triangle is Isoscles")
