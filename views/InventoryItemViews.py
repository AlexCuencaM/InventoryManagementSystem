from models.InventoryItem import InventoryItem
class InventoryItemViews:

    def get_inventory_items_view(self, data: list[InventoryItem]) -> None:
        repeated_characters = 10
        for product_on_inventory in data:
            product_title = product_on_inventory.name
            dynamic_line = ('-' * ((repeated_characters * 2) + len(product_title)))
            print(dynamic_line)
            print(('-' * repeated_characters) + product_title + ('-' * repeated_characters))
            print("Product id: " + str(product_on_inventory.product_id))
            print("Current stock: " + str(product_on_inventory.current_stock) )
            print("Initial stock: " + str(product_on_inventory.initial_stock) )
            print(dynamic_line)
            print("Commercial Name: " + product_on_inventory.product.title)
            print("Qty of suppliers: " + str(len(product_on_inventory.product.suppliers)))
            for sup in product_on_inventory.product.suppliers:
                print(dynamic_line)
                print("Supplier name: " + sup.name)    
                print("Supplier address: " + sup.address)
                print(dynamic_line)
            print(dynamic_line)
            print(dynamic_line)
            # print("----------------------------------------------")
    def modify_inventory_items_view(self, item:InventoryItem | None) -> None:
        if(item is None):
            print("Product not found :(")
            return
        print("MODIFY product with ID: " + str(item.product_id))
        item.name = input("Inventory Product name: ")
        item.category = input("Category: ")
        item.product.title = input("Commercial product name: ")
        item.current_stock = self.current_stock_input()
        item.product.price = self.price_input()
    
    def current_stock_input(self):
        try:
            return int(input("Current stock: ")) 
        except ValueError:
            print("The current_stock must be an integer")
            return self.current_stock_input()
    
    def price_input(self):
        try:
            return float(input("Current stock: ")) 
        except ValueError:
            print("The id must be a number")
            return self.price_input()

    def search_product_by_id(self) -> int:
        try:
            return int(input("Search the product on inventory by id: ")) 
        except ValueError:
            print("The id must be an integer")
            return self.search_product_by_id()
