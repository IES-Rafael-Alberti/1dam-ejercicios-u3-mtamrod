def almacenar_asig(n_asig) -> list:
    asignaturas = []
    for i in range (n_asig):
        asignatura = str(input("Introduce la asignatura: "))
        asignaturas.append(asignatura)
    return print(asignaturas)

def main():
    n_asig = int(input("¿Cuántas asignaturas quiere introducir?: "))
    almacenar_asig(n_asig)
    
      
if __name__ == "__main__":
    main()