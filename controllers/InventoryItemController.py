from repositories.InventoryItemRepository import InventoryItemRepository
from views.InventoryItemViews import InventoryItemViews
class InventoryItemController:
    def __init__(self, repository, inventory_items_view):
        self.__repository:InventoryItemRepository  = repository
        self.__inventory_items_view: InventoryItemViews = inventory_items_view
    def get_inventory_items(self) -> None:
        data = self.__repository.get_inventory_items()
        self.__inventory_items_view.get_inventory_items_view(data)
        
    def modify_inventory_items(self) -> None:
        id = self.__inventory_items_view.search_product_by_id()
        data = self.__repository.get_inventory_items_by_id(id)
        self.__inventory_items_view.modify_inventory_items_view(data)
        self.__repository.update_inventory_item(data)

    def create_inventory_items(self) -> None:
        id = self.__inventory_items_view.search_product_by_id()
        data = self.__repository.get_inventory_items_by_id(id)
        new_item = self.__inventory_items_view.create_inventory_items_view(data, id)
        self.__repository.insert_inventory_item(new_item)

    def delete_inventory_item(self) -> None:
        id = self.__inventory_items_view.search_product_by_id()
        has_deleted = self.__repository.delete_inventory_item(id)
        self.__inventory_items_view.delete_inventory_item_view(has_deleted)
