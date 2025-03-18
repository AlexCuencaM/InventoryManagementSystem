from controllers.InventoryItemController import InventoryItemController
class PrincipalMenuView:
    def __init__(self, controller:InventoryItemController):
        self.controller = controller

    def mostrar_menu(self):
        """Muestra el menú de opciones al usuario."""
        print("\n=== MENÚ DE GESTIÓN DE INVENTARIOS ===")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Modificar stock")
        print("4. Consultar productos")
        print("5. Guardar y Salir")
    def choose_option(self) -> int:
        try:
            return int(input("Choose an option: ")) 
        except ValueError:
            print("[ERROR] Opción no válida, intente de nuevo.")
            return self.choose_option()
        
    def select_view(self, option:int) -> None | bool:
        if option == 1:
            print("*****Crear productos*****")
            self.controller.create_inventory_items()
        elif option == 2:
            print("*****Borrar productos*****")
            self.delete_product()
        elif option == 3:
            print("*****Modificar productos*****")
            self.controller.modify_inventory_items()
        elif option == 4:
            print("*****Consultar productos*****")
            self.controller.get_inventory_items()
        elif option == 5:
            return self.exit_menu()
        else:
            print("[ERROR] Opción no válida, intente de nuevo")
    
    def create_product(self):
        pass
    def modify_product(self):
        pass
    def delete_product(self):
        pass
    def select_product(self):
        pass
    def exit_menu(self) -> bool:
        print("[INFO] Saliendo del sistema...")
        return True