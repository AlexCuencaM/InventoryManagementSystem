from InventoryContext import InventoryContext
from models.InventoryItem import InventoryItem
class InventoryItemRepository:
    def __init__(self, context):
        self.context: InventoryContext = context
    def get_inventory_items(self) -> list[InventoryItem]:
        return self.context.inventory_items

        