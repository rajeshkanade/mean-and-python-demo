# Initialize product dictionary
products = {}

def add_product(product_id, name, price, stock):
    products[product_id] = {"name": name, "price": price, "stock": stock}

def update_stock(product_id, quantity):
    if product_id in products:
        if products[product_id]["stock"] >= quantity:
            products[product_id]["stock"] -= quantity
            print(f"✅ Purchase successful! Remaining stock: {products[product_id]['stock']}")
            return True
        else:
            print("❌ Not enough stock available!")
    else:
        print("❌ Product not found!")
    return False

def display_low_price_products():
    print("\n🛍️ Products priced below 1000:")
    found = False
    for prod_id, prod in products.items():
        if prod["price"] < 1000:
            found = True
            print(f"ID: {prod_id}, Name: {prod['name']}, Price: {prod['price']}, Stock: {prod['stock']}")
    if not found:
        print("No products below 1000.")

# --- Main program ---
n = int(input("Enter number of products to add: "))

for i in range(n):
    print(f"\nEnter details for Product {i+1}:")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Product Price: "))
    stock = int(input("Product Stock: "))
    add_product(product_id, name, price, stock)

# Display products below 1000
display_low_price_products()

# Allow user to make a purchase
choice = input("\nDo you want to purchase a product? (yes/no): ").strip().lower()
if choice == "yes":
    product_id = input("Enter Product ID to purchase: ")
    qty = int(input("Enter quantity: "))
    update_stock(product_id, qty)

# Final list of products
print("\n📦 Updated Product List:")
for pid, p in products.items():
    print(f"ID: {pid}, Name: {p['name']}, Price: {p['price']}, Stock: {p['stock']}")
