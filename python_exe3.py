num = int(input('Digite um numero: '))
lista = []
numero = num
cont=1

while(num>9):
    a = num%10
    num = num//10
    lista.append(a)
    
    if num<10:
        lista.append(num)
        
    
   
aux=10
novo_num = 0
cont2 = 1
tam = len(lista)
for i in range(tam):
    novo_num += lista[i]*(aux**(tam-cont2))
    cont2 +=1
if numero==novo_num:
    print('eh um palindromo')
else:
    print('nao eh um palindromo')
