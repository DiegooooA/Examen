#productos={modelo:[marca, pantalla, RAM, disco, GB de DD, procesador, video]}

productos={'8475HD':['HP',15.6,'8GB','DD','1T','Intel core i5','NVIDIA GTX1050'],'2175HD':['Acer',14,'4GB','SSD','512GB','Intel core i5','NVIDIA GTX1050']}

stock={'8475HD':[387990,31],'2175HD':[327990,43],'JjfFHD':[424990,1],'fgdxFHD':[664990,21],'123FHD':[290890.32],'342FHD':[444990,7]
       ,'GF75HD':[749990,2],'UWU131HD':[349990,1],'fs1230hd':[249990,0]}

def stock_marca(marca):
    productos_marca = [modelo for modelo, detalles in productos.items() if detalles[0].lower() == marca.lower()]
    if not productos_marca:
        print(f"No se encontraron productos de la marca {marca}.")
        return

    print(f"Productos de la marca {marca}:")
    for modelo in productos_marca:
        if modelo in stock:
            cantidad = stock[modelo]
            print(f"Cantidad en stock: {cantidad}")
        else:
            print(f"Modelo: {modelo} no tiene información de stock disponible.")



def buscar_por_precio(precio_min, precio_max):
    encontrados = []
    for modelo, detalles in stock.items():
        precio = detalles[0]
        if precio_min <= precio <= precio_max:
            encontrados.append(modelo)

    if encontrados:
        print("Productos encontrados en el rango de precios:")
        for modelo in encontrados:
            print(f"Modelo: {modelo}, Precio: {stock[modelo][0]}, Cantidad: {stock[modelo][0]}")
    else:
        print("No se encontraron productos en el rango de precios especificado.")

def eliminar_producto(modelo):
    if modelo in stock:
        del stock[modelo]
        print("Producto eliminado.!!!")
















def mostar_menu():
    print("1. Stock Marca")
    print("2.Busqueda por precio ")
    print("3. Eliminar Producto")
    print("4. Salir")

def main():
    while True:
        mostar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion=="1":
            marca = input("Ingrese la marca del producto: ")
            stock_marca(marca)
        elif opcion=="2":
            precio_min = int(input("Ingrese el precio mínimo: "))
            precio_max = int(input("Ingrese el precio máximo: "))
            buscar_por_precio(precio_min, precio_max)
        elif opcion=="3":
            modelo = input("Ingrese el modelo del producto a eliminar: ")
            eliminar_producto(modelo)
            rep=int(input("Desea eliminar otro producto? 1. Si 2. No: "))
            if rep == 1:
                continue
            elif rep == 2:
                print("Saliendo del programa.")
                break
        elif opcion=="4":
            print(" Programa finalizado.")
            break
        else:
            print("Debe Seleccionar una opción válida!!. ")

main()

