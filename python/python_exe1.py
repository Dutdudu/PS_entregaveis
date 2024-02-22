lista = []
i = 1
print('Digite 0 para parar de inserir valores')
while(i!=0):
    i = int(input('Digite um valor: '))
    if i == 0:
        break
    lista.append(i)
tam = len(lista)
if lista[0]==lista[tam-1]:
    print('São iguais')
else:
    print('Não são iguais')
