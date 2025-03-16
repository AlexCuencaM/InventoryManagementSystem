from models.InventoryItem import InventoryItem
import json
class InventoryContext:
    def __init__(self):
        self.inventory_items:list[InventoryItem] = self.__get_inventory_items()

    def __read_inventory_items(self) -> list[dict]:
        f = open('db.json')
        json_data = json.load(f)
        results = json_data['inventory_items']
        return results
    
    def __get_inventory_items(self)-> list[InventoryItem]:
        json_data = self.__read_inventory_items()
        results: list[InventoryItem] = []
        for items in json_data:
            for item in items.items():
                new_inventory_item = InventoryItem()
                new_inventory_item.name = items['name']
                new_inventory_item.category = items['category']
                new_inventory_item.current_stock = items['current_stock']
                new_inventory_item.initial_stock = items['initial_stock']
                new_inventory_item.product_id = items['product_id']
                # for product in item['product'].items():
                new_inventory_item.product.title = items['title.product']
                results.append(new_inventory_item)
        return results

