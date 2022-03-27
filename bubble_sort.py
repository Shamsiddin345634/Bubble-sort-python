l = [1,8,6,10,12,3,7,5,4,0,9,11]
for j in range(len(l)):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            new = l[i]
            l[i] = l[i+1]
            l[i+1] = new
print(l)