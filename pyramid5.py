import string
alpha = string.ascii_lowercase

num=int(input("enter num\n"))
for i in range (0,num,+1):
    print(" " * (i), end="")
    for j in range (i,num,+1):

        print(alpha[j],end="")
    print("\r")


