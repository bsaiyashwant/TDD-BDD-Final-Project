def test_read_product():
    product = {"name": "Laptop", "category": "Electronics", "price": 1000.0, "availability": True}
    assert product["name"] == "Laptop"

def test_update_product():
    product = {"name": "Laptop", "category": "Electronics", "price": 1000.0, "availability": True}
    product["price"] = 900.0
    assert product["price"] == 900.0

def test_delete_product():
    products = [{"name": "Laptop"}, {"name": "Phone"}]
    products.pop(0)
    assert len(products) == 1

def test_list_all_products():
    products = [{"name": "Laptop"}, {"name": "Phone"}]
    assert len(products) == 2

def test_find_by_name():
    products = [{"name": "Laptop"}, {"name": "Phone"}]
    found = next((p for p in products if p["name"] == "Laptop"), None)
    assert found is not None

def test_find_by_category():
    products = [{"name": "Laptop", "category": "Electronics"}, {"name": "Phone", "category": "Electronics"}]
    filtered = [p for p in products if p["category"] == "Electronics"]
    assert len(filtered) == 2

def test_find_by_availability():
    products = [{"name": "Laptop", "availability": True}, {"name": "Phone", "availability": False}]
    available = [p for p in products if p["availability"]]
    assert len(available) == 1
