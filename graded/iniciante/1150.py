for i in range (0,1):
    x=int(input())
    z=int(input())
    soma=0
    cont=1
    while not (x<z):
        z=int(input())
    for i in range (x,(z+1)):
        soma+=i
        if soma<z:
            cont+=1
        elif soma>=z:
            print(cont)
            break
