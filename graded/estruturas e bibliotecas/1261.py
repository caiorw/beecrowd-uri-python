palavras,jobs=[int(x) for x in input().split()]
total=0
controle=0
if palavras<=1000 and jobs<=100:
    dicpontos={}
    for pal in range(palavras):
        a=input().split()
        if (len(a[0])<=16) and (0<=int(a[1])<=1000000):
            dicpontos[a[0].lower()]=int(a[1])
    while controle<jobs:
        descricao=input().split(" ")
        if "." not in descricao:
            for tag in dicpontos.keys():
                total+=(descricao.count(tag)*dicpontos[tag])
        else:
            print(total)
            controle+=1
            total=0
