from calcular import calculate_total
from facturacion import generar_factura
from resumen import mostrar_resumen

def main():
    ventas = {}
    continuar = "si"
    total_recaudado = 0

    print("===========================")
    print("Welcome to Nuvexa shop!!!")
    print("===========================")
    print("REGISTRO DE VENTAS\n")

    while continuar.lower() == "si":
        producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad vendida: "))

        total_venta = calculate_total(precio, cantidad)
        total_recaudado += total_venta

        generar_factura(producto, precio, cantidad, total_venta)

        if producto in ventas:
            ventas[producto]["cantidad"] += cantidad
        else:
            ventas[producto] = {"cantidad": cantidad}

        continuar = input("¿Desea registrar otra venta? (si/no): ")

    mostrar_resumen(ventas, total_recaudado)

if __name__ == "__main__":
    main()