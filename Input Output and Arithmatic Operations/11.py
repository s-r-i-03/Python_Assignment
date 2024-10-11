amt = int(input("Enter the amount to be withdrawn: "))
hun_dred = amt // 100  
rem = amt % 100  

if rem != 0:
    fif_ty = rem // 50 
    rem = rem % 50  
else:
    fif_ty = 0

if rem != 0:
    tens = rem // 10 
else:
    tens = 0

print("We need:")
if hun_dred > 0:
    print(f"{hun_dred} numbers of 100rs notes")
if fif_ty> 0:
    print(f"{fif_ty} numbers of 50rs notes")
if tens> 0:
    print(f"{tens} numbers of 10rs notes")


