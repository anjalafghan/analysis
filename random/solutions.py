totalCustomers = int(input())
l = []
for customers in range(totalCustomers):
    
    l.append(int(input()))

l.sort()
print(l)
k = []
fixedValue = l[-2]
for el in l:
    if el >=fixedValue:
        k.append(el)
sum = fixedValue * len(k)