while True:
    try:
        n=int(input())
        if 1<=n<=100000:
            epr=0
            ehd=0
            intruso=0
            for a in range(n):
                aluno=input().split()
                if aluno[1].upper()=='EPR':
                    epr+=1
                elif aluno[1].upper()=='EHD':
                    ehd+=1
                else:
                    intruso+=1
            print(f"EPR: {epr}")
            print(f"EHD: {ehd}")
            print(f"INTRUSOS: {intruso}")
    except EOFError:
        break
