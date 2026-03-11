def mostrar_resumen(ventas, total_recaudado):
 print("\nRESUMEN  DE VENTAS DEL DIA: ")
 for producto, datos in ventas:
  print ("Producto: ", producto)
  print("Cantidad total vendida: ", datos["cantidad"])
  print()
  print("TOTAL RECAUDO DEL DIA: ", total_recaudado)
