c1 = 0
c4 = 0
cM = 0
cont = 0
sumM = 0
sumF = 0
sumNeto = 0

def leedatoc():
    return input("Genero (M: masculino F: femenino): ").upper()

def leedatoe():
    return int(input("Tipo de Libro (1: Ficcion 2: Novelas 3: Cuentos 4: Fisica Cuantica): "))

def ingreso():
    global c1, c4, cM, cont, sumM, sumF, sumNeto

    gen = ''
    while gen != 'M' and gen != 'F':
        gen = leedatoc()

    tipo = 0
    while tipo < 1 or tipo > 4:
        tipo = leedatoe()

    cant = 0
    while cant <= 0:
        cant = int(input("Cantidad de libros: "))

    precios = {1: 90, 2: 100, 3: 80, 4: 150}
    precio = precios[tipo]

    if cant <= 2:
        descuentos = {1: 0.05, 2: 0.08, 3: 0.09, 4: 0.02}
        porc = descuentos[tipo]
    elif 3 <= cant <= 6:
        descuentos = {1: 0.06, 2: 0.16, 3: 0.18, 4: 0.02}
        porc = descuentos[tipo]
    else:
        descuentos = {1: 0.08, 2: 0.32, 3: 0.36, 4: 0.04}
        porc = descuentos[tipo]

    bruto = cant * precio
    dcto = bruto * porc
    neto = bruto - dcto

    print("\nImporte a pagar:", bruto)
    print("Descuento:", dcto)
    print("Importe Neto:", neto)

    if tipo == 4:
        c4 += 1
    if tipo == 1 and porc == 0.06:
        c1 += 1
    if gen == 'M' and 200 <= dcto <= 2500:
        cM += 1
    sumNeto += neto

    if gen == 'F' and tipo == 2:
        sumF += neto
    if gen == 'M' and tipo == 3:
        sumM += neto
        cont += 1

def reporte():
    global c1, c4, cM, cont, sumM, sumF, sumNeto
    prom = sumM / cont if cont > 0 else 0

    print("\n------ REPORTE ------")
    print("Cantidad ventas de Fisica Cuantica:", c4)
    print("Cantidad ventas de Ficcion y dcto 6%:", c1)
    print("Cantidad ventas Varones y dcto [200,2500]:", cM)
    print("Total Importe Neto:", sumNeto)
    print("Total Neto Mujeres y Novelas:", sumF)
    print("Promedio Neto de Varones y Cuentos:", prom)

def main():
    global c1, c4, cM, cont, sumM, sumF, sumNeto

    opcion = 0
    while opcion != 3:
        print("\n----------------------")
        print(" MENU ")
        print("----------------------")
        print("[1] Registrar Venta")
        print("[2] Reportar Venta")
        print("[3] Salir")
        print("----------------------")
        
        opcion = int(input("Opcion: "))

        if opcion == 3:
            print("Fin del Programa")

        if opcion > 3:
            print("ERROR!!!!, DEBE INGRESAR UNA OPCION DEL 1 al 3")

        if opcion == 1:
            ingreso()
        elif opcion == 2:
            reporte()

    print("FIN DE PROCESO")

if __name__ == "__main__":
    main()

