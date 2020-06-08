num=int(input())
arr=[]
j=1
for i in range(0,num,+1):
        arr.append(j)
        j=j+2
size=(arr[num-1])
j=num-1
for x in arr:
    print(j * " ",end="")
    j=j-1
    print(x * "*")