def numperfeito (n):
    divisores=[]
    soma=0
    for d in range(1,n):
        if n%d==0:
            divisores.append(d)
    for num in divisores:
        soma+=num
    if soma==n:
        return True
    else:
        return False
n=int(input())
while not 1<=n<=20:
    n=int(input())    
for i in range(1,n+1):
    x=int(input())
    if numperfeito(x):
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
