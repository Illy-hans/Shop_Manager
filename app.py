
from lib.order_repository import OrderRepository
from lib.item_repository import ItemRepository
from lib.item import Item
from lib.order import Order 
from lib.database_connection import DatabaseConnection
import inquirer 

class Application():

    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/shop_manager.sql")

    def run(self):
        print("\nWelcome to your shop management program!\n")

        print(
                "Here are your options:\n"
                "\n1: List all shop items\n"
                "2: Create a new shop item\n"
                "3: List all orders\n"
                "4: Create new order\n"
                "5: Look up an order and return all the items in the order\n"
                )
        
        answer = input("Choose one here: ")

        if answer == '1':
            item_repository = ItemRepository(self._connection)
            items = item_repository.all()
            for item in items:
                print(f"#{item.id}: {item.name} - £{item.unit_price}(price p/u) - {item.quantity} in stock")

        elif answer == '2':
            item_repository = ItemRepository(self._connection)
            new_item_name = input("Add new name: ")
            new_item_unit_price = input("Add new price: ")
            new_item_quantity = input("Add quanitity: ")
            new_item = Item(None, new_item_name, new_item_unit_price, new_item_quantity)
            item_repository.add(new_item)
            items = item_repository.all()
            print(f"\nHere is your updated item list:\n")
            for item in items:
                print(f"#{item.id}: {item.name} - £{item.unit_price}(price p/u) - {item.quantity} in stock")
        
        elif answer =='3':
            order_repository = OrderRepository(self._connection)
            orders = order_repository.all()
            for order in orders:
                print(f"#{order.id} - Customer name: {order.customer_name} - Date of order: {order.order_date}")

        elif answer == '4':
            order_repository = OrderRepository(self._connection)
            new_order_name = input("\nAdd customer name: ")
            new_order_date = input("Add order date: ")

            item_repository = ItemRepository(self._connection)
            all_items = item_repository.all()
            print("\nHere is your current inventory:")
            for item in all_items:
                print(f"#{item.id}: {item.name} - £{item.unit_price}(price p/u) - {item.quantity} in stock")

            # questions = [
            # inquirer.Checkbox('options',
            #         message="Add items:\n",
            #         choices=[Item(1, "Coffee Grinder", 19.99, 20),
            #                 Item(2, "Coffee Beans", 11.99, 10),
            #                 Item(3, "Espresso Maker", 349.99, 13),
            #                 Item(4, "Coffee Machine Cleaner", 24.50, 30)],
            #         ),
            #         ]
            
            # item = inquirer.prompt(questions)
            # print(item)

            item_to_add_to_order = int(input("Enter item id: "))
            item_to_add = item_repository.find_item(item_to_add_to_order)

            #new_order = Order(None, new_order_name, new_order_date, item_to_add)
            order_repository.add_order(Order(None, new_order_name, new_order_date), item_to_add, None)
            orders = order_repository.all()
            print(f"\nHere is your updated order list:\n")
            for order in orders:
                print(f"#{order.id} - Customer name: {order.customer_name} - Date of order: {order.order_date}")
        
        elif answer =='5':
            order_repository = OrderRepository(self._connection)
            order_number = input("Please enter the order number: ")
            result = order_repository.find_with_items(order_number)
            print(f"\nOrder:{result.id} -- Customer name: {result.customer_name} -- Date of order: {result.order_date}")
            for item in result.items:
                print(f"#{item.id}: {item.name} - £{item.unit_price}(price p/u)")
        #Does not deal with the exception of the order number being out of range 
        else:
            print("Choose a valid option")



if __name__ == '__main__':
    app = Application()
    app.run()
