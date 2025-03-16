from models.InventoryItem import InventoryItem
class InventoryItemViews:
    def get_inventory_items_view(self, data: list[InventoryItem]) -> None:
        print(data)
        # for product_on_inventory in data:
        #     print(product_on_inventory)
            # print(product_on_inventory.name)
            # print(product_on_inventory.product.suppliers)
