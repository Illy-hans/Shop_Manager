#   3 = list all orders When I call OrderRepository.all all orders are returned
#   4 = create a new order When I call OrderRepository.create a new order is created 

import datetime
from lib.order_repository import OrderRepository
from lib.order import Order
from lib.item import Item

"""
When I call OrderRepository.all 
all orders are returned
"""

def test_return_all_orders(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    result = repository.all()
    assert result == [
        Order(1, "Yaz", datetime.date(2023,10,22)),
        Order(2, "Ali", datetime.date(2023,11,29)),
        Order(3, "Maya", datetime.date(2023,11,20)),
        Order(4, "Ruby", datetime.date(2023,12,1))
    ]


"""
When I call OrderRepository.find_with_items
the order with the items is returned 
"""

def test_find_with_items(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)
    
    result = repository.find_with_items(2)
    assert result == Order(2, "Ali", datetime.date(2023,11,29), [
        Item(1, "Coffee Grinder", 19.99, 20),
        Item(4, "Coffee Machine Cleaner", 24.50, 30)
    ])


"""
When I create an order with OrderRepository.create
a new order is created with 1 item 
"""

def test_new_order(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    repository.add_order(Order(5, "Jane", datetime.date(2023,12,2)), [Item(1, "Coffee Grinder", 19.99, 20)])

    assert repository.all() == [
        Order(1, "Yaz", datetime.date(2023,10,22)),
        Order(2, "Ali", datetime.date(2023,11,29)),
        Order(3, "Maya", datetime.date(2023,11,20)),
        Order(4, "Ruby", datetime.date(2023,12,1)),
        Order(5, "Jane", datetime.date(2023,12,2))
    ]


"""
When I create an order with OrderRepository.create
a new order is created with 2 items
"""

def test_new_order(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    repository.add_order(Order(5, "Jane", datetime.date(2023,12,2)), [Item(1, "Coffee Grinder", 19.99, 20), Item(4, "Coffee Machine Cleaner", 24.50, 30)])

    assert repository.all() == [
        Order(1, "Yaz", datetime.date(2023,10,22)),
        Order(2, "Ali", datetime.date(2023,11,29)),
        Order(3, "Maya", datetime.date(2023,11,20)),
        Order(4, "Ruby", datetime.date(2023,12,1)),
        Order(5, "Jane", datetime.date(2023,12,2))
    ]