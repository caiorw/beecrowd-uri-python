a, b, c = input().split()

a = float(a)
b = float(b)
c = float (c)

tri = a*c/2
tri = f"{tri:.3f}"

cir = 3.14159*c*c
cir = f"{cir:.3f}"

tra = (a+b)*c/2
tra = f"{tra:.3f}"

qua = b*b
qua = f"{qua:.3f}"

ret = a*b
ret = f"{ret:.3f}"

print("TRIANGULO:",tri)
print("CIRCULO:",cir)
print("TRAPEZIO:",tra)
print("QUADRADO:",qua)
print("RETANGULO:",ret)
