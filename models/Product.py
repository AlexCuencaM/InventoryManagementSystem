from models.Supplier import Supplier
class Product:
    def __init__(self):
        self.id = None
        self.title = ""
        self.price = 0
        self.suppliers:list[Supplier] = []