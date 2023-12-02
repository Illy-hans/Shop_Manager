#   1 = list all shop items When I call ItemRepository.all all items are returned
#   2 = create a new item When I call ItemRepository.add an item is added nothing is returned 

from lib.item_repository import ItemRepository
from lib.item import Item

"""
When I call ItemRepository.all 
all items in the shop are returned

"""
def test_all_items_are_returned(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    items = repository.all()
    assert items == [
        Item(1, "Coffee Grinder", 19.99, 20),
        Item(2, "Coffee Beans", 11.99, 10),
        Item(3, "Espresso Maker", 349.99, 13),
        Item(4, "Coffee Machine Cleaner", 24.50, 30)
    ]


"""
When I call ItemRepository.add an item is added 
nothing is returned 
"""

def test_add_item(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    repository.add(Item(None, "KeepCup", 12.50, 99))

    assert repository.all() == [
        Item(1, "Coffee Grinder", 19.99, 20),
        Item(2, "Coffee Beans", 11.99, 10),
        Item(3, "Espresso Maker", 349.99, 13),
        Item(4, "Coffee Machine Cleaner", 24.50, 30),
        Item(5, "KeepCup", 12.50, 99)
    ]

"""
When I call Itemrepository.find_item
it returns the Item
"""

def test_find_item(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)

    result = repository.find_item(2)
    assert result == Item(2, "Coffee Beans", 11.99, 10)