
p=[5,2,8]
for x in p:
    print ('*' * x)

for x in 'piatia':
    print(x,end=" ")

for x in ['pia','lomi','riata']:
    print(x,end=" ")

for x in range(5):
    print(x,end=" ")

for x in range(5,10):
    print(x,end=" ")

for x in range(5,10,2):
    print(x,end=" ")

price=[10,20,30]
sum=0
for x in price:
    sum+=x
print(sum)

for x in range(3):
    for y in range (3):
        print( f'({x},{y})')