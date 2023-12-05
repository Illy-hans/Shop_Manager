from lib.order import Order
from lib.item import Item

class OrderRepository():
    
    def __init__(self, connection):
        self._connection = connection 

    def all(self):
        rows = self._connection.execute('SELECT * FROM orders')
        orders = []
        for row in rows:
            order = Order(row["id"], row["customer_name"], row["order_date"])
            orders.append(order)
        
        return orders 
    
    def find_with_items(self, order_id):
        rows = self._connection.execute('SELECT items.id AS items_id, items.name, items.unit_price, items.quantity, orders.id AS order_id, orders.customer_name, orders.order_date FROM items JOIN items_orders ON items_orders.item_id = items.id JOIN orders ON items_orders.order_id = orders.id WHERE orders.id = %s', [order_id])
        items = []
        for row in rows:
            row = Item(row["items_id"], row["name"], row["unit_price"], row["quantity"])
            items.append(row)

        return Order(rows[0]["order_id"], rows[0]["customer_name"], rows[0]["order_date"], items)
        
    
    def add_order(self, order, items):
        self._connection.execute('INSERT INTO orders (customer_name, order_date) VALUES (%s, %s)', [order.customer_name, order.order_date])
        for item in items:
            self._connection.execute('INSERT INTO items_orders(item_id, order_id) VALUES (%s, %s)', [item.id, order.id])

        return None


