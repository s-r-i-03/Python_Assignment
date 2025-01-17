cost=int(input("Enter the cost:"))
sell_price=int(input("Enter the selling price:"))
if sell_price>cost:
    print("Seller has made profit")
    print("profit",end="")#end parameter specifies what should be printed at the end, which is \n by default, but we're setting it to "" so new line doesnt occur
else:
    print("Seller has incurred loss")   
    print("loss",end="") 
print(" is", sell_price-cost)