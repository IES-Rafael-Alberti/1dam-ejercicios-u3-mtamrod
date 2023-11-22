def pedir_numero():
    numeros = []
    for i in range (6):
        num = str(input("Introduce los 6 números ganadores: "))
        numeros.append(num)
    #mayor_menor(numeros)
    
#def mayor_menor(numeros):
    
    
def main():
    pedir_numero()
    
    
if __name__ == "__main__":
    main()
    
"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""