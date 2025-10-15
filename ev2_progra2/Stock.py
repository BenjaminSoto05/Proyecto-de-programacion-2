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

    def descontar_ingrediente(self, nombre: str, cantidad: float) -> bool:
        for i, ingrediente in enumerate(self.lista_ingredientes):
            if ingrediente.nombre.lower() == nombre.lower():
                if self.lista_ingredientes[i].cantidad >= cantidad:
                    self.lista_ingredientes[i].cantidad -= cantidad
                    # Opcional: eliminar si la cantidad llega a 0
                    if self.lista_ingredientes[i].cantidad == 0:
                        self.lista_ingredientes.pop(i)
                    return True
                else:
                    return False  # No hay suficiente stock
        return False  # El ingrediente no se encontró

    def eliminar_ingrediente(self, nombre_ingrediente: str):
        self.lista_ingredientes = [
            ing for ing in self.lista_ingredientes if ing.nombre.lower() != nombre_ingrediente.lower()
        ]

    def verificar_stock(self):
        pass

    def actualizar_stock(self, nombre_ingrediente, nueva_cantidad):
        pass

    def obtener_elementos_menu(self):
        pass
