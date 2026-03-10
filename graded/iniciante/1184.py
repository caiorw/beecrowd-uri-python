linha=[0] * 12
matriz=[linha] * 12
o=input().upper()
soma,count=0,0
for line in range(12):
    linha=[]      
    for column in range(12):
        linha.append(float(input()))
    matriz[line]=linha

for l in range(12):
    for c in range(12):
        if l>c:
            soma+=matriz[l][c]
            count+=1
if o=='S':
    print(f'{soma:.1f}')
elif o=='M':
    media = soma/count
    print(f'{media:.1f}')
