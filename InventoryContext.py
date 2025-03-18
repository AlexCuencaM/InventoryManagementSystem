from models.InventoryItem import InventoryItem
from models.Supplier import Supplier
import json
class InventoryContext:
    def __init__(self):
        self.inventory_items:list[InventoryItem] = self.__adapt_from_json()

    def __read_inventory_items(self) -> list[dict]:
        f = open('db.json')
        json_data = json.load(f)
        results = json_data['inventory_items']
        return results
    def __adapt_from_json(self)-> list[InventoryItem]:
        json_data = self.__read_inventory_items()
        results: list[InventoryItem] = []
        for items in json_data:
            new_inventory_item = InventoryItem()
            new_inventory_item.name = items['name']
            new_inventory_item.category = items['category']
            new_inventory_item.current_stock = items['current_stock']
            new_inventory_item.initial_stock = items['initial_stock']
            new_inventory_item.product_id = items['product_id']
            new_inventory_item.product.title = items['product']['title']
            new_inventory_item.product.price = items['product']['price']
            for supplier in items['product']['suppliers']:
                db_supplier = Supplier()
                db_supplier.address = supplier['address']
                db_supplier.id = supplier['id']
                db_supplier.name = supplier['name']
                new_inventory_item.product.suppliers.append(db_supplier)
            results.append(new_inventory_item)
        return results

    def save_changes(self) -> None:
        with open("db.json", "w") as outfile:
            json.dumps(self.inventory_items, outfile)