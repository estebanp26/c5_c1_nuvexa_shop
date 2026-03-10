def registrar_ventas():
	total_recaudado=0
	ventas={}

	continuar="si"

	while continuar=="si":
		producto=input("Ingrese el nombre del producto: ")
		precio = float(input("Ingrese el precio del producto: "))
		cantidad = int(input("Ingrese la cantidad vendida: "))
		total_venta=precio*cantidad
		total_recaudado+=total_venta
		if producto in ventas:
			ventas[producto]+=total_venta
		else:
			ventas[producto] = cantidad
		continuar = input("¿Deseas registrar otra venta? si/no").lower()
	return ventas, total_recaudado