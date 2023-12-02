from lib.order import Order 

"""
Order constructs with an id, customer_name, order_date
"""
def test_order_constructs():
    order = Order(1, "Test name", '2023-12-02')
    assert order.id == 1
    assert order.customer_name == "Test name"
    assert order.order_date == '2023-12-02'

"""
We can format items to strings nicely
"""
def test_orders_format_nicely():
    order = Order(1, "Test name", '2023-12-02')
    assert str(order) == "Order(1, Test name, 2023-12-02)"


"""
We can compare two identical orders
And have them be equal
"""
def test_orders_are_equal():
    order1 = Order(1, "Test name", '2023-12-02')
    order2 = Order(1, "Test name", '2023-12-02')
    assert order1 == order2 
