import string
alpha = string.ascii_uppercase

num=int(input("enter num\n"))
for i in range (0,num,+1):
    for j in range (i,num,+1):
        print(alpha[j],end="")
    print(" " * (num - i))

