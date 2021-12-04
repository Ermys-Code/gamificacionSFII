def LeerTablaMultiplicarLineaN():
    n = int(input("Introduce un numero entero entre 1 y 10: "))
    m = int(input("Introduce otro numero entero entre 1 y 10: "))
    fileName = "tabla-" + str(n) + ".txt"
    try:
        f = open(fileName, "r")
    except:
        print("No existe el fichero con la tabla del ", n)
    else:
        lines = f.readlines()
        f.close()

LeerTablaMultiplicarLineaN()