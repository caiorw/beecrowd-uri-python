while True:
    try:
        vetor=[]
        for entrada in range(11):
            vetor.append(int(input()))
            if vetor[entrada]<=0:
                vetor[entrada]=1
            print(f"X[{entrada}] = {vetor[entrada]}")
    except EOFError:
        break
