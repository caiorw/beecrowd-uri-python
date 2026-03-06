n=int(input())
tabuleiro=[]
for j in range(n):
    tabuleiro.append(0)
    
for i in range(n):
    bomba=int(input())
    if bomba==1:
        tabuleiro[i]+=1
        if i<n-1:
            tabuleiro[i+1]+=1
        if 0<i:
            tabuleiro[i-1]+=1

for k in tabuleiro:
    print(k)
