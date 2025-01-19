from behave import given
from service.models import Product, db

@given('the following products exist')
def step_impl(context):
    
    db.session.query(Product).delete()
    db.session.commit()

    sample_products = [
        {"id": 1, "name": "Smartphone", "category": "Electronics", "price": 699.99, "available": True},
        {"id": 2, "name": "Laptop", "category": "Electronics", "price": 999.99, "available": False},
        {"id": 3, "name": "Headphones", "category": "Accessories", "price": 49.99, "available": True},
        {"id": 4, "name": "Coffee Mug", "category": "Kitchenware", "price": 9.99, "available": True},
        {"id": 5, "name": "Gaming Chair", "category": "Furniture", "price": 199.99, "available": False},
        {"id": 6, "name": "Backpack", "category": "Travel", "price": 39.99, "available": True},
        {"id": 7, "name": "Action Camera", "category": "Electronics", "price": 299.99, "available": True},
        {"id": 8, "name": "Desk Lamp", "category": "Furniture", "price": 24.99, "available": True},
        {"id": 9, "name": "Air Purifier", "category": "Appliances", "price": 129.99, "available": False},
        {"id": 10, "name": "Wireless Mouse", "category": "Accessories", "price": 19.99, "available": True}
    ]

    # Add each product to the database
    for product_data in sample_products:
        product = Product(
            id=product_data["id"],
            name=product_data["name"],
            category=product_data["category"],
            price=product_data["price"],
            available=product_data["available"]
        )
        db.session.add(product)

    # Commit the changes to the database
    db.session.commit()
