from lib.item import Item

"""
Item constructs with an id, name, unit_price, quantity
"""
def test_item_constructs():
    item = Item(1, "Test item", 12.33, 45)
    assert item.id == 1
    assert item.name == "Test item"
    assert item.unit_price == 12.33
    assert item.quantity == 45

"""
We can format items to strings nicely
"""
def test_items_format_nicely():
    item = Item(1, "Test item", 12.33, 45)
    assert str(item) == "Item(1, Test item, 12.33, 45)"


"""
We can compare two identical items
And have them be equal
"""
def test_items_are_equal():
    item1 = Item(1, "Test item", 12.33, 45)
    item2 = Item(1, "Test item", 12.33, 45)
    assert item1 == item2
