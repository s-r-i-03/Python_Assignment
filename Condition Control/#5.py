num= int(input("Enter the number:"))
number=num
rev=0
while(num!=0):
    rem= num%10
    rev= rev*10+rem
    num=num//10
if(rev==number):
    print("Palindrome number")    
else:
    print("not palindrome")    
