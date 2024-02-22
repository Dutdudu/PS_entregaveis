num = int(input('Digite um numero: '))
for i in range(1,num):
    if (num%i)==0:
        aux = 0
        for e in range(2,i):
            if (i%e)==0:
                aux = 1
        if aux == 0:
            maior_divisor = i

if maior_divisor == 1:
    print(f'O numero {num} eh primo') 
else:       
    print(f'O maior divisor primo de {num} eh {maior_divisor}')