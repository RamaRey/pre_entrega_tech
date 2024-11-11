opcion = ""
lista_producto = [{"nombre":"coca", "stock":5},
                  {"nombre":"pepsi","stock":7}
                  ]

while opcion != "4":
        print ("\n--- SISTEMA DE STOCK BEBIDAS ---")
        print ("\n1) Agregar Producto")
        print ("2) Control de Stock")
        print ("3) Generar Reporte Productos")
        print ("4) Salir")

        opcion = input("\nIngrese la opcion deseada: ")

        if opcion == "1":
                #Un bucle con un submenu, para seguir agregando productos o volver al menu principal
                opcion_producto = ""
                while opcion_producto != "2":
                    print("\n--- AGREGAR PRODUCTO ---")
                    print ("\n1) Desea ingresar un producto?")
                    print ("2) Menu principal")
                    print("")
                    opcion_producto = input("Ingrese la opcion deseada: ")
                    if opcion_producto == "1":
                        producto = input("\ningrese un producto: ")
                        stock = int(input("Ingrese el stock: "))
                        #Bucle para controlar que el stock siempre sean numeros positivos.
                        while stock <= 0:
                            print("\nSolo se permite stock positivo")
                            stock = int(input("\nIngrese el stock correcto: "))
                        disc_producto = { "nombre":producto,"stock":stock }
                        lista_producto.append(disc_producto)
                        print (f"\nEl producto", producto, "fue AGREGADO con exito")
                        print(f"Su stock es",stock,"unidades")
                        print("")
                    elif opcion_producto == "2":
                        break
                    else:
                        print("\n--- OPCION INCORRECTA!!!")

        elif opcion == "2":
            producto = input("\nIngrese el nombre del producto que quiere buscar: ")
            contador = 0
            #Bucle para encontrar el producto
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
            #Un For para imprimir la lista completa.
            print("\n--- REPORTE INVENTARIO ---")
            for producto in lista_producto:
                print ("\nProducto:", producto['nombre'])
                print ("Stock:", producto['stock'])

        elif opcion == "4":
            #Sale del sistema y finaliza la APP.
            print("\nGRACIAS POR USAR EL SISTEMA")
            print("")
            break
       
        else:
            print("\n--- OPCION INCORRECTA!!!")
            print("\ningrese opcion correcta")
            print("")
