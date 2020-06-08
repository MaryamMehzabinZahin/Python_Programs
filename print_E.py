import string

num=int(input())
ar=[]
for i in range(1,num+1,+1):
    if i%2==0:
        ar.append(2)
    else:
        ar.append(5)
for x in ar:
    print("*" * x)
