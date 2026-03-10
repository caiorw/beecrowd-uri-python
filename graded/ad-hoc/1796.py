q=int(input())
while not 4<=q<=233000:
    q=int(input())
v=list(map(int, input().split()))
if v.count(0)>v.count(1):
    print("Y")
else:
    print("N")
