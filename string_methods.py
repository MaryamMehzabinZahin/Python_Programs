import string
alpha = string.ascii_uppercase
for i in range(0,3,1):
    for j in range(i,3,+1):
        print(alpha[j],end=" ")
    print('\n')

