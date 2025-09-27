# An e-commerce app wants to store details of products in a dictionary
# ({product_id: [name, price, stock]}). Write Python code to:
# - Add a new product
# - Update stock after purchase
# - Display all products with price less than 1000

# Initialize product dictionary
products = {}

def add_product(product_id, name, price, stock):
    products[product_id] = {"name": name, "price": price, "stock": stock}

def update_stock(product_id, quantity):
    if product_id in products and products[product_id]["stock"] >= quantity:
        products[product_id]["stock"] -= quantity
        return True
    return False

def display_low_price_products():
    return [prod for prod_id, prod in products.items() if prod["price"] < 1000]

# Example usage
add_product("P001", "Laptop", 1200, 10)
add_product("P002", "Mouse", 500, 50)
update_stock("P002", 2)
print(products)
print(display_low_price_products())