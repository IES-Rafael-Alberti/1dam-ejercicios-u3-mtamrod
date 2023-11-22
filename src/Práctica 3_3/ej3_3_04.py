def funct_frutas_solo_en_frutas2(set_frutas1, set_frutas2):
    frutas_solo_en_frutas2 = set_frutas2 - set_frutas1
    
    return print(f"Las frutas unicas de frutas2 son: {frutas_solo_en_frutas2}")

def funct_frutas_solo_en_frutas1(set_frutas1, set_frutas2):
    frutas_solo_en_frutas1 = set_frutas1 - set_frutas2
    
    return print(f"Las frutas unicas de frutas1 son: {frutas_solo_en_frutas1}")

def funct_frutas_comunes(set_frutas1, set_frutas2):
    frutas_comunes = set_frutas1 | set_frutas2
    
    return print(f"Las frutas comunes son: {frutas_comunes}")
    
def crear_conjuntos(frutas1, frutas2):
    set_frutas1 = set(frutas1) 
    set_frutas2 = set(frutas2)
    
    return set_frutas1, set_frutas2

def main():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    
    set_frutas1, set_frutas2 = crear_conjuntos(frutas1, frutas2)
    funct_frutas_comunes(set_frutas1, set_frutas2)
    funct_frutas_solo_en_frutas1(set_frutas1, set_frutas2)
    funct_frutas_solo_en_frutas2(set_frutas1, set_frutas2)
    
if __name__ == "__main__":
    main()