# a=1
# b=4
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if (i!=j and j!=k and i!=k):
                print(i,j,k)