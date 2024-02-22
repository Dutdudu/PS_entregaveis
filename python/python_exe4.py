num = 2
for i in range(3,1000):
    aux = 0
    for e in range(2,i):
        if (i%e)==0:
            aux = 1
    if aux==0:
        num += i
print(num)
        
        
