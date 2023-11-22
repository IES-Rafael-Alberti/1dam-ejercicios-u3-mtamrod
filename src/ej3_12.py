def col_mult(matriz1, matriz2) -> tuple:
    return tuple(fil_mult(matriz1[i], matriz2[i]) for i in range(len(matriz1)))

def fil_mult(matriz1, matriz2) -> tuple:
    return tuple(matriz1[i]*matriz2[i] for i in range(len(matriz1)))

def main():
    matriz1 = ([1, 2]
              ,[3, 4]
              ,[5, 6])
    
    matriz2 = ([-1, 0]
              ,[0, 1]
              ,[1, 1])  
      
    print(f"{matriz1} * {matriz2} = \n{col_mult(matriz1, matriz2)}")
    
if __name__ == "__main__":
    main()