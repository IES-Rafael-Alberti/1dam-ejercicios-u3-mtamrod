def almacenar_asig(n_asig) -> list:
    asignaturas = []
    for i in range (n_asig):
        asignatura = str(input("Introduce la asignatura: "))
        asignaturas.append(asignatura)
    recorrer_asig(asignaturas)

def recorrer_asig(asignaturas):
    for asignatura in asignaturas:
        print(f"Yo estudio {asignatura}.")

def main():
    n_asig = int(input("¿Cuántas asignaturas quiere introducir?: "))
    almacenar_asig(n_asig)
    
if __name__ == "__main__":
    main()
