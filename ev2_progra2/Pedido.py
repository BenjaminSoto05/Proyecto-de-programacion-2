from ElementoMenu import CrearMenu
from typing import List


class Pedido:
    def __init__(self):
        self.menus = []

    def agregar_menu(self, menu: CrearMenu):
        ok = True # Variable para evitar bucle?
        for menu_exs in self.menus:
            if menu.nombre == menu_exs.nombre:
                menu_exs.cantidad += 1
                ok = False
        if ok:
            # Creamos una copia para no modificar el menú original del catálogo
            nuevo_menu = CrearMenu( # Instancia de CrearMenu, aplica atributos
                nombre=menu.nombre,
                ingredientes=menu.ingredientes,
                precio=menu.precio,
                icono_path=menu.icono_path,
                cantidad=1
            )
            self.menus.append(nuevo_menu) # Cada instancia se le asigna una lista, lista que se rellena con 

    def eliminar_menu(self, nombre_menu: str):
        i = 0
        for menu in self.menus:
            if nombre_menu == menu.nombre: # Si la cantidad es mayor a 1, restale 1, si es contrario, borralo, 1 !> 1
                if menu.cantidad > 1:
                    menu.cantidad -= 1
                else:
                    del self.menus[i]
            i += 1

    def get_lista_menus(self) -> List[CrearMenu]:
        return list(self.menus.values())

    def mostrar_pedido(self):
        pass

    def calcular_total(self) -> float:
        total = 0.0
        for menu in self.menus:
            total += menu.precio * menu.cantidad
        return total