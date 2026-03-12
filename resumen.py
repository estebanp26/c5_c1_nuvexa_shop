def mostrar_resumen(ventas, total_recaudado):
    print("-----------------------------------")
    print("\nDAILY SALES SUMMARY: ")
    for producto, datos in ventas.items():
        print(f"Product: {producto}, Total quantity sold: {datos['cantidad']}")
        print("-----------------------------------")
    print(f"TOTAL COLLECTED FOR THE DAY: {total_recaudado}")