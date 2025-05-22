import math
def raizes_reais():
    a = float(input("Digite o coeficiente A: "))
    b = float(input("Digite o coeficiente B: "))
    c = float(input("Digite o coeficiente C: "))
    delta = b**2 - 4*a*c
    if delta >= 0:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print("As raízes reais são: ")
    else:
        print("Essa equação não possuí raízes reais.")

raizes_reais()
