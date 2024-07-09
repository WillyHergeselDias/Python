import math
x1 = 0
x2 = 0
a = float(input("Informe A:"))
b = float(input("Informe B:"))
c = float(input("Informe C:"))
Delta = (b*b-4*a*c)
print(f'Valor do delta: {Delta}')
if Delta < 0:
    print("Erro: Delta negativo, não exitem raízes reais!")
else:
    RDelta = math.sqrt(Delta)
    print(f'Raiz quadrada do delta: {RDelta}')
    x1 = (-b + RDelta)/(2*a)
    x2 = (-b - RDelta)/(2*a)
    print(f'Primeira raiz: {x1}')
    print(f'Segunda raiz: {x2}')

