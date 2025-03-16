from repositories.InventoryItemRepository import InventoryItemRepository
from views.InventoryItemViews import InventoryItemViews
class InventoryItemController:
    def __init__(self, repository, inventory_items_view):
        self.__repository:InventoryItemRepository  = repository
        self.__inventory_items_view: InventoryItemViews = inventory_items_view
    def get_inventory_items(self) -> None:
        data = self.__repository.get_inventory_items()
        self.__inventory_items_view.get_inventory_items_view(data)

