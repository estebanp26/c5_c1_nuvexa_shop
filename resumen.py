def mostrar_resumen(ventas, total_recaudado):
    print("-----------------------------------")
    print("\nRESUMEN DE VENTAS DEL DIA: ")
    for producto, datos in ventas.items():
        print(f"Producto: {producto}, Cantidad total vendida: {datos['cantidad']}")
        print("-----------------------------------")
    print(f"TOTAL RECAUDADO DEL DIA: {total_recaudado}")