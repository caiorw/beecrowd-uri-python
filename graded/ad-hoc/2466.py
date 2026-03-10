n=int(input())
while not 2<=n<=64:
    n=int(input())
fileira=list(int(x) for x in input().split())
for t in range(n):
    if len(fileira)!=1:
        prox=[]
        for b in range(len(fileira)):
            if b==len(fileira)-1:
                pass
            else:
                if fileira[b]+fileira[b+1] in [-2,2]:
                    prox.append(1)
                else:
                    prox.append(-1)
        fileira=prox[:]
    else:
        if 1 in fileira:
            print('preta')
        else:
            print('branca')
