lista_producto = [{"nombre":"coca", "stock":5},
                  {"nombre":"pepsi","stock":7}
                  ]

while True:
        print ("\n--- SISTEMA DE STOCK BEBIDAS ---")
        print ("\n1) Agregar Producto")
        print ("2) Control de Stock")
        print ("3) Generar Reporte Productos")
        print ("4) Salir")

        opcion = input("\nIngrese la opcion deseada: ")

        if opcion == "1":
            print("\n--- AGREGAR PRODUCTO ---")
            print("")
            producto = input("ingrese un producto: ")
            stock = input("Ingrese el stock: ")
            if stock == type (int):
                disc_producto = { "nombre":producto,"stock":stock }
                lista_producto.append(disc_producto)
                print (f"\nEl producto", producto, "fue agregado con exito")
                print(f"Su stock es",stock,"unidades")
                print("")
            else:
                print("\nEl stock debe ser ingresado en valores numericos")

        elif opcion == "2":
            producto = input("\nIngrese el nombre del producto que quiere buscar: ")
            contador = 0
            while contador < len(lista_producto):
                if lista_producto[contador]["nombre"] == producto:
                    print("\n<-- PRODUCTO ENCONTRADO -->")
                    print(f"\nProducto: {lista_producto[contador]['nombre']}")
                    print(f"Stock:", stock)
                    print("")
                    break
                contador = contador + 1
                if contador == len(lista_producto):
                    print(f"\nEl producto {producto} no se encuentra en stock.")
                    print("")

        elif opcion == "3":
            print("\n--- REPORTE INVENTARIO ---")
            for producto in lista_producto:
                print ("\nProducto:", producto['nombre'])
                print ("Stock:", producto['stock'])

        elif opcion == "4":
            print("\nGRACIAS POR USAR EL SISTEMA")
            print("")
            break
       
        else:
            print("\n--- OPCION INCORRECTA!!!")
            print("\ningrese opcion correcta")
            print("")
