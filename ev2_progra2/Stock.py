from Ingrediente import Ingrediente


class Stock:
    def __init__(self):
        self.lista_ingredientes = []

    def agregar_ingrediente(self, nuevo_ingrediente: Ingrediente):
        for i, existente in enumerate(self.lista_ingredientes):
            # Busca por nombre y unidad
            if existente.nombre.lower() == nuevo_ingrediente.nombre.lower() and existente.unidad == nuevo_ingrediente.unidad:
                self.lista_ingredientes[i].cantidad = int(
                    self.lista_ingredientes[i].cantidad) + int(nuevo_ingrediente.cantidad)
                return  # Termina la función

        # Si no lo encontró en el bucle, lo agrega como nuevo
        self.lista_ingredientes.append(nuevo_ingrediente)

    def eliminar_ingrediente(self, nombre_ingrediente: str):
        self.lista_ingredientes = [
            ing for ing in self.lista_ingredientes if ing.nombre.lower() != nombre_ingrediente.lower()
        ]

    def verificar_stock(self, menu):
        # Definición True por default: Se define False si no se cumplen las condiciones
        suficiente_stock = True
        if self.lista_ingredientes == []:
            suficiente_stock = False
        for ingrediente_necesario in menu.ingredientes:
            print(ingrediente_necesario)
            for ingrediente_stock in self.lista_ingredientes:
                if ingrediente_necesario.nombre == ingrediente_stock.nombre:
                    if int(ingrediente_stock.cantidad) < int(ingrediente_necesario.cantidad):
                        return False
            if not suficiente_stock:
                break
        if suficiente_stock == True:
            return True

    def actualizar_stock(self, nombre_ingrediente: str, nueva_cantidad: float):
        """
        Busca un ingrediente por su nombre y actualiza su cantidad.
        Devuelve True si lo encontró y actualizó, False en caso contrario.
        """
        for ingrediente in self.lista_ingredientes:
            # Busca el ingrediente ignorando mayúsculas/minúsculas
            if ingrediente.nombre.lower() == nombre_ingrediente.lower():
                ingrediente.cantidad = nueva_cantidad
                return True  # Indica que la operación fue exitosa
        return False  # Indica que no se encontró el ingrediente

    def obtener_elementos_menu(self, umbral: int = 5):
        """
        Revisa el inventario y devuelve una lista de los ingredientes
        cuya cantidad es igual o menor al umbral especificado.

        Args:
            umbral (int): La cantidad mínima que activa la alerta de bajo stock.

        Returns:
            list: Una lista de objetos Ingrediente que necesitan ser repuestos.
        """
        lista_para_comprar = []
        for ingrediente in self.lista_ingredientes:
            # Aplica la lógica solo para ingredientes contados por unidad
            if ingrediente.unidad == "unid" and ingrediente.cantidad <= umbral:
                lista_para_comprar.append(ingrediente)
        return lista_para_comprar
