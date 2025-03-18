from InventoryContext import InventoryContext
from models.InventoryItem import InventoryItem
class InventoryItemRepository:
    def __init__(self, context):
        self.context: InventoryContext = context
    def get_inventory_items(self) -> list[InventoryItem]:
        return self.context.inventory_items
    
    def get_inventory_items_by_id(self, id:int) -> InventoryItem | None:
        current_inventory_item = next((ie for ie in self.get_inventory_items() if ie.product_id == id), None)
        return current_inventory_item
    def insert_inventory_item(self, item:InventoryItem) -> None:
        self.context.inventory_items.append(item)
        self.context.save_changes()
    def update_inventory_item(self, item:InventoryItem | None) -> None:
        if item is None:
            return
        current_inventory_item = self.get_inventory_items_by_id(item.product_id)
        self.context.inventory_items.remove(current_inventory_item)
        self.insert_inventory_item(item)
        self.context.save_changes()
    def delete_inventory_item(self, id:int) -> bool:
        has_deleted = False
        current_inventory_item = self.get_inventory_items_by_id(id)
        if(current_inventory_item is None):
            return has_deleted
        self.context.inventory_items.remove(current_inventory_item)
        self.context.save_changes()
        has_deleted = True
        return has_deleted