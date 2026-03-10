linha=[0] * 12
matriz=[linha] * 12

linhaoperacao=int(input())
while not 0<=linhaoperacao<=11:
    linhaoperacao=int(input())

operacao=input().upper()
soma=0

for line in range(12):
    linha=[]      
    for column in range(12):
        linha.append(float(input()))
    matriz[line]=linha

if operacao=="S":
    for n in matriz[linhaoperacao]:
        soma+=n
    print(soma)

elif operacao=="M":
    for n in matriz[linhaoperacao]:
        soma+=n
    print(soma/12)
