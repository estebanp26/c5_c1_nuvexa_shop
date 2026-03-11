from calcular import calcular_total
from facturacion import generar_factura
from resumen import  mostrar_resumen

print("===========================")
print("Welcome to Nuvexa shop!!!")
print("===========================")

ventas={}
continuar = "si"
total_recaudado=0
print("REGISTRO DE VENTAS\n")
while continuar=="si":
    producto=input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad vendida: "))
    continuar =input("¿Desea registrar otra venta? (si/no)").lower()
    
total_venta = calcular_total(precio, cantidad)

total_recaudado += total_venta

generar_factura (producto, precio, cantidad, total_venta)

if producto in ventas:
 ventas[producto] ["cantidad"]+= cantidad
else:
 ventas[producto] = {"cantidad" : cantidad}

mostrar_resumen(ventas, total_recaudado)
 
