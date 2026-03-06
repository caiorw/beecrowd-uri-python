n=int(input())
for casos in range(n):
    produtos={}
    compras={}
    m=int(input())
    for i in range(m):
        produto=input().split()
        produtos[produto[0]]=float(produto[1])
    p=int(input())
    for j in range(p):
        compra=input().split()
        compras[compra[0]]=int(compra[1])
    
    total=0
    for k,v in compras.items():
        for p,c in produtos.items():
            if k==p:
                total+=v*c
    print(f"R$ {total:.2f}")
