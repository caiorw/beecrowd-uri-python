n=int(input())
numeros=list(map(int, input().split()))
mult2=0
mult3=0
mult4=0
mult5=0
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        mult2 += 1
    if numeros[i] % 3 == 0:
        mult3 += 1
    if numeros[i] % 4 == 0:
        mult4 += 1
    if numeros[i] % 5 == 0:
        mult5 += 1
print(f"{mult2} Multiplo(s) de 2")
print(f"{mult3} Multiplo(s) de 3")
print(f"{mult4} Multiplo(s) de 4")
print(f"{mult5} Multiplo(s) de 5")
