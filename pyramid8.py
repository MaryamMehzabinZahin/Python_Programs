num=int(input())
arr=[]
arr2=[]
j=1
for i in range(0,num,+1):
        arr.append(j)
        j=j+2
arr.reverse()
j=1
for x in arr:
        print(x * "*")
        print(j * " ", end="")
        j=j+1
print("\r")
j1=1
for x in arr:
        print(x * "*")
        print(j1 * " ", end="")
        j1=j1+1

