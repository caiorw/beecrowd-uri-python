n=0
r=1
while r!=0:
    aldo,beto=0,0
    r=int(input())
    resultado="padrao"
    for i in range(r):
        a,b=input().split()
        aldo+=int(a)
        beto+=int(b)
    if aldo>beto:
        resultado="Aldo"
    elif beto>aldo:
        resultado="Beto"
    n+=1
    if r!=0:
        print(f"Teste {n}")
        print(resultado)
        print()
