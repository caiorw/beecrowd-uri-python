while True:
  try:
    def verifica(x):
        while not(1<=x<=10**4):
            x=int(input())
        return x
    
    def verifica_nr(n,r):
        while not(r<=n):
            r=int(input())
        return r 
    u,r=map(int, input().split())
    x=list(map(int, input().split()))
    if(u==r):
      print("*")
    else:
      p=""
      naovoltaram=[]
      for j in range(0,u):
        naovoltaram.append(j+1)
      for i in range(0,len(naovoltaram)):
        count=0
        for k in range(0,len(x)):
          if(naovoltaram[i]==x[k]):
            count+=1
        if(count==0):
          p+=str(naovoltaram[i]) + " "
      print(p)
  except EOFError:
    break
