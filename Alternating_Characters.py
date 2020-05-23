iteration = int(input())
count=[]
for _ in range(iteration):
    j=0
    count1 = 0;
    word = input()
    for i in range(len(word) - 1):

        if word[i] == word[i + 1]:
            count1 += 1
    count.append(count1)

for x in range(len(count)):
    print (count[x])