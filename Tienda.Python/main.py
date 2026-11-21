class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def mostrar(self):
        print(f"{self.nombre} - ${self.stock}")
class Tienda:
    def __init__(self):
        self.productos = []
    def agregar_productos(self):
        self.productos = []z
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Producto agregado correctamente")
    def mostrar_productos(self):
        if len(self.productos) == 0:
            print("No hay productos.")
        else:
            for producto in self.productos:
                producto.mostrar()
    def comprar(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                if cantidad <= 0:
                    print("Cantidad invalida.")
                elif cantidad > producto.stock:
                    print("No hay suficiente stock.")
                else:
                    producto.stock -= cantidad
                    total = producto.precio * cantidad
                    print("COmpra realizada")
                    print("Total: $", total)
                    return
        print("Producto no encontrado.")
tienda = Tienda()
while True:
    print("MI TIENDA")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Mostar producto")
    print("4. Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = input("Precio: ")
        stock = input("Cantidad disponible: ")
        if precio.isdigit() and stock.isdigit():
            precio = int(precio)
            stock = int(stock)
            if precio > 0  and stock >= 0:
                producto = Producto(nombre, precio, stock)
                tienda.agregar_producto(producto)
            else:
                print("Debes ingresar numeros validos.")
        else:
            print("Debes ingresar numeros validos.")
    elif opcion == "2":
        tienda.mostrar_productos()
    elif opcion == "3":
        nombre = input("Producto que deseas comprar: ")
        cantidad = input("Cantidad: ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            tienda.comprar(nombre, cantidad)
        else:
            print("Debes ingresar una cantidad valida.")
    elif opcion == "4":
        print("Gracias por visitar la tienda")
        break
    else:
        print("Opcion incorrecta")