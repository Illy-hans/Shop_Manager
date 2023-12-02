from lib.item import Item

class ItemRepository():
    
    def __init__(self, connection):
        self._connection = connection


    def all(self):
        rows = self._connection.execute('SELECT * FROM items')
        items = []
        for row in rows:
            product = Item(row["id"], row["name"], row["unit_price"], row["quantity"])
            items.append(product)
        return items


    def add(self, item):
        self._connection.execute('INSERT INTO items (name, unit_price, quantity) VALUES (%s, %s, %s)', [item.name, item.unit_price, item.quantity])
        return None
    

    def find_item(self, item_id):
        rows = self._connection.execute('SELECT * from items WHERE id = %s', [item_id])
        row = rows[0]
        return Item(row["id"], row["name"], row["unit_price"], row["quantity"])

