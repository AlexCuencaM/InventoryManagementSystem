from controllers.InventoryItemController import InventoryItemController
from repositories.InventoryItemRepository import InventoryItemRepository
from views.InventoryItemViews import InventoryItemViews
from InventoryContext import InventoryContext
# Defining main function
def main():
    context = InventoryContext()
    repo = InventoryItemRepository(context)
    view = InventoryItemViews()
    controller = InventoryItemController(repo, view)
    controller.get_inventory_items()

if __name__=="__main__":
    main()

