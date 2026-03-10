conector1=list(map(int, input().split()))
conector2=list(map(int, input().split()))
somas=[]

for k in range(5):
    somas.append(conector1[k]+conector2[k])

if somas.count(1)!=5:
    print("N")
else:
    print("Y")
