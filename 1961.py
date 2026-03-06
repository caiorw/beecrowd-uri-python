def verifica (men,x,mai):
    while not(men<=x<=mai):
        x=int(input())
    return x

controle=1
p,n=map(int, input().split())
p=verifica(1,p,5)
n=verifica(2,n,100)
alturas=list(map(int, input().split()))

for i in range(1,n):
    d=alturas[i-1]-alturas[i]
    if d<0:
        d=d*(-1)
    if d>p:
        print("GAME OVER")
        controle-=1
if controle==1:
    print("YOU WIN")
