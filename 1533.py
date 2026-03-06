while True:
    try:
        n=int(input())
        if n==0:
            break
        suspeitos=list(map(int, input().split()))

        pessoas=suspeitos[:]
        suspeitos.sort()
        print(1+pessoas.index(suspeitos[-2]))
    except EOFError:
        break
