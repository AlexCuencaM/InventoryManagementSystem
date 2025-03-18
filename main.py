from controllers.InventoryItemController import InventoryItemController
from repositories.InventoryItemRepository import InventoryItemRepository
from views.InventoryItemViews import InventoryItemViews
from InventoryContext import InventoryContext
from MenuBuilder import MenuBuilder
# Defining main function
def main():
    context = InventoryContext()
    repo = InventoryItemRepository(context)
    view = InventoryItemViews()
    controller = InventoryItemController(repo, view)
    menu = MenuBuilder(controller)
    menu.build()

if __name__=="__main__":
    main()

