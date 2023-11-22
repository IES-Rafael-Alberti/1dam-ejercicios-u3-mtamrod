def interseccion_pares_multiplos3(pares, multiplos_de_tres):
   pares_y_multiplos_de_tres = pares & multiplos_de_tres
   
   print(f"La intersección entre ambos es: {pares_y_multiplos_de_tres}")

def conjunto_multiplos3(lista_numeros:set):
    lista_multiplo_de_tres = []
    
    for numero_lista in lista_numeros:
        if numero_lista%3==0:
            lista_multiplo_de_tres.append(numero_lista)
            multiplos_de_tres = set(lista_multiplo_de_tres)
    
    print(f"Los multiplos de tres son: {multiplos_de_tres}")
    
    return multiplos_de_tres
    
def conjunto_pares(lista_numeros:set):
    lista_pares = []
    
    for numero_lista in lista_numeros:
        if numero_lista%2==0:
            lista_pares.append(numero_lista)
            pares = set(lista_pares)
        
    print(f"Los pares son: {pares}")
    
    return pares
        
def conjunto_a_lista(numeros):
    lista_numeros = list(numeros)
    
    return lista_numeros

def main():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    lista_numeros = conjunto_a_lista(numeros)
    pares = conjunto_pares(lista_numeros)
    multiplos_de_tres = conjunto_multiplos3(lista_numeros)
    interseccion_pares_multiplos3(pares, multiplos_de_tres)
    
if __name__ == "__main__":
    main()
