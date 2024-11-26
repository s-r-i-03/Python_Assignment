x,y=map(int,input("Enter the value ofx and y:").split())
if x==0 and y==0:
    print("The coordinate lies at the origin")
elif x!=0 and y==0:
    print("The coordinate lies on x-axis")
else:
    print("The coordinate lies on y-axis")        
