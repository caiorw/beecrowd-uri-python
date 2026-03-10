x=int(input())
if 3<=x<=20:
    presentes={}
    for p in range(x):
        a=input().split(" ")
        presentes[a[0].lower()]=a[1:]
while True:
    try:
        chute=input().split(" ")
        if chute[0] in presentes.keys():
            if chute[1] in presentes[chute[0]]:
                print("Uhul! Seu amigo secreto vai adorar o/")
            else:
                print("Tente Novamente!")
        else:
            print("Tente Novamente!")
    except EOFError:
        break
