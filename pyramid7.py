num=int(input())
arr=[]
arr2=[]
j=1
for i in range(0,num,+1):
        arr.append(j)
        j=j+2

arr2=(arr[:-1])
size=(arr[num-1])
j=num-1
for x in arr:
    print(j * " ",end="")
    j=j-1
    print(x * "*")
arr.reverse()
del arr[0]
j=1
for x in arr:
    if x!=0:
        print(j * " ", end="")
        j=j+1
        print(x * "*")