num=int(input("enter num\n"))
for i in range (1,num+1,+1):
    print(" " * (num-i),end="")
    print("*" * i)
