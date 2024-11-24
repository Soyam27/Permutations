x = input("enter the number whose permutations you want:")
l =[]
pro = 1
a = list(x)
for i in range(0,len(a)):
    freq = 1
    for j in range(i+1,len(a)):
        if a[i] == a[j] and a[i]!="":
            freq = freq +1
            a[j] = ""
    if freq>1:
        l.append(freq)
for i in range(1,len(x)+1):
    pro = pro*i

if len(l)>0:
    for j in range(0,len(l)):
        for k in range(0,l[j]):
            pro = pro/(l[j]-k)
print("Total no. of permutations:")
print(pro)

import random
l = []
y = list(x)
print("possible numbers:")
while len(l)!=pro:
    random.shuffle(y)
    z = ''.join(y)
    
    if z not in l:
        l.append(z)
    print(z)
print("Array of permutated numbers:")
print(l)
