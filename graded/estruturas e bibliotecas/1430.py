notas={'W':1,'H':1/2,'Q':1/4,'E':1/8,'S':1/16,'T':1/32,'X':1/64}
while True:
    try:
        compos=input()
        if "*" not in compos:
            duracao1=0
            compos=compos[1:-1].split("/")
            for compasso in compos:
                tempo=0
                for nota in compasso:
                    tempo+=notas[nota]
                if tempo==1:
                    duracao1+=1
            print(duracao1)
    except EOFError:
        break
