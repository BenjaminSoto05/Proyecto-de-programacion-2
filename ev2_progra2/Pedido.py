from ElementoMenu import CrearMenu 
from typing import List

class Pedido:
    def __init__(self):
        self.menus = {}
        
    def agregar_menu(self, menu: CrearMenu):
        if menu.nombre in self.menus:
            self.menus[menu.nombre].cantidad += 1
        else:
            # Creamos una copia para no modificar el menú original del catálogo
            nuevo_menu = CrearMenu(
                nombre=menu.nombre,
                ingredientes=menu.ingredientes,
                precio=menu.precio,
                icono_path=menu.icono_path,
                cantidad=1
            )
            self.menus[menu.nombre] = nuevo_menu

    def eliminar_menu(self, nombre_menu: str):
        if nombre_menu in self.menus:
            if self.menus[nombre_menu].cantidad > 1:
                self.menus[nombre_menu].cantidad -= 1
            else:
                del self.menus[nombre_menu]

    def get_lista_menus(self) -> List[CrearMenu]:
        return list(self.menus.values())

    def mostrar_pedido(self):
        pass

    def calcular_total(self) -> float:
        total = 0.0
        for menu in self.menus.values():
            total += menu.precio * menu.cantidad
        return total
