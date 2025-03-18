from controllers.InventoryItemController import InventoryItemController
from views.PrincipalMenuView import PrincipalMenuView
class MenuBuilder:
    def __init__(self, inventory_controller: InventoryItemController):
        self.controller = inventory_controller

    def build(self):
        menu  = PrincipalMenuView(self.controller)
        """Función principal que ejecuta la aplicación de inventario."""
        while True:
            menu.mostrar_menu()
            option = menu.choose_option()
            hasExited = menu.select_view(option)
            if hasExited is not None:
                break