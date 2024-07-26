# primer ejercicio bucle 
for n in range (8):
    print(n)

print('-----------------------')

for n in range (1, 13):
    print(n)

# segundo ejerciico bucle
# primero desde donde empieza, el segundo donde termina y el tercero de cuanto en cuanto  
for n in range (3, 100,3): 
    print(n)
    
# contar de atras hacia adelante 
for n in range (10, 0, -1):
    print(n)
    
print("¡Despegue!")

# condigo de la tortuga 
from turtle import*

for n in range (4):
    forward(100)
    right(90)