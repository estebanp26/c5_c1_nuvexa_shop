def mostrar_resumen(ventas, total_recaudado):
 print("----------------------------------")
 print("\nRESUMEN  DE VENTAS DEL DIA: ")
 for producto, datos in ventas:
     print ("Producto: ", producto["producto"])
     print("Cantidad total vendida: ",datos ["cantidad"])
     print("TOTAL RECAUDO DEL DIA: ", total_recaudado)
