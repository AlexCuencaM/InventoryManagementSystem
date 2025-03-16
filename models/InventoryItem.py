from models.Product import Product
class InventoryItem:
    def __init__(self):
        self.product_id = None
        self.name = ""
        self.category = ""
        self.initial_stock = 0
        self.current_stock = 0
        self.product: Product = Product()