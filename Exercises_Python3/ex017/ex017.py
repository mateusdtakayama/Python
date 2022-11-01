import math
import math

adj = float(input("Insira o cateto adjacente: "))
oposto = float(input("Insira o cateto oposto: "))

hip = ((adj**2+oposto**2))**0.5 ## (1/2)
hip2  = math.hypot(adj, oposto)
print(hip)
print(hip2)