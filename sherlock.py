# Python 3 code to demonstrate
# Maximum frequency character in String
# naive method

# initializing string
test_str = input()

# printing original string


# using naive method to get
# Maximum frequency character in String
all_freq = {}
count={}
m={}
c=0
flag=0
t=0
v=0
for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1
res = max(all_freq, key = all_freq.get)
res1 = min(all_freq, key = all_freq.get)
min1=all_freq[res1]
max1=all_freq[res]
# printing result


p=len(all_freq)
for i in all_freq:
    if all_freq[i]>min1:
        c=c+1
        count=all_freq[i]


for i in all_freq:
    for j in all_freq:
        if i!=res1 and j!=res1:
            if int(all_freq[i])!=int(all_freq[j]):
                flag=1

if p>1:
    if c>1:
        if min1>1:
            print("NO")
        elif c==1:
            if count-min1==1 :
                print("YES")
        elif min1==1:
            if flag==1:
                print("NO")
            if flag==0:
                print("YES")
    else:
        print("NO")
else:
    print("YES")