while True:
    n=int(input())
    if 1<=n<=50:
        falsas=0
        assinaturas={}
        for aluno in range(n):
            assina=input().split()
            assinaturas[assina[0].capitalize()]=assina[1]
        m=int(input())
        if 0<=m<=n:
            for presente in range(m):
                assina=input().split()
                count=0
                verifica=assinaturas[assina[0].capitalize()]
                for letra in range(len(assina[1])): 
                    if assina[1][letra]!=verifica[letra]:
                        count+=1
                if count>1:
                    falsas+=1
            print(falsas)
        else:
            break
    else:
        break
