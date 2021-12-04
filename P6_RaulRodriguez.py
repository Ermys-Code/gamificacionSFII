from os.path import exists

def LeerTablaMultiplicar():
    n = int(input("Introduce un numero entero entre 1 y 10: "))
    fileName = "tabla-" + str(n) + ".txt"
    try:
        f = open(fileName, "r")
    except FileNotFoundError:
        print("No existe el fichero con la tabla del", n)
    else:
        print(f.read())
    f.close()

LeerTablaMultiplicar()

fileExist = exists("./tabla-5.txt")

print(fileExist)