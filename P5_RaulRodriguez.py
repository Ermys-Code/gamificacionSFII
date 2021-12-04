def tablaMultiplicar():
    n = int(input("Introduce un numero entero entre 1 y 10: "))
    fileName = "tabla-" + str(n) + ".txt"
    f = open(fileName, "w")
    for i in range(1, 11):
        f.write(str(n) + " x " + str(i) + " = " + str(n * i) + "\n")
    f.close()

tablaMultiplicar()