num=int(input("enter the number"))

for i in range(num,0,-1):
    print("*" * i )

for i in range(0,num,+1):
    for j in range(i,num,+1):
        print("*",end="")
    print("\n")