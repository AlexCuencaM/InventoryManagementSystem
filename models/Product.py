from models.Supplier import Supplier
class Product:
    def __init__(self):
        self.id = None
        self.title = ""
        self.suppliers:list[Supplier] = []