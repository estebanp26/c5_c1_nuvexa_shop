#Call the function when you need it
from calcular import calculate_total
from facturacion import generar_factura
from resumen import mostrar_resumen

def main():
    ventas = {}   #Empty dictionary to store all products
    continuar = "yes"
    total_recaudado = 0

    print("===========================")
    print("Welcome to Nuvexa shop!!!")
    print("===========================")
    print("SALES RECORD\n")

    while continuar.lower() == "yes":
        producto = input("Enter the product name: ")    
        precio = float(input("Enter the product price: "))
        cantidad = int(input("Enter the quantity sold: "))

        total_venta = calculate_total(precio, cantidad)
        total_recaudado += total_venta

        generar_factura(producto, precio, cantidad, total_venta)

        if producto in ventas:
            ventas[producto]["cantidad"] += cantidad
        else:
            ventas[producto] = {"cantidad": cantidad}

        continuar = input("Do you want to register another sale? (yes/no): ")

    mostrar_resumen(ventas, total_recaudado)

if __name__ == "__main__":   #Only run the main function if this file is running.
    main()