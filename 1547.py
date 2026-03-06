n=int(input())

for casos in range(n):
    qt,s=map(int, input().split())
    chutesgrupos=list(map(int, input().split()))
    for j in range(qt):
        chutesgrupos[j]=abs(s-chutesgrupos[j])
    
    ordenados=chutesgrupos[:]
    ordenados.sort()
    ganhador=chutesgrupos.index(ordenados[0])
    print(ganhador+1)
