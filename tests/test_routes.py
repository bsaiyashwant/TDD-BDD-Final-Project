def test_read_route(client):
    response = client.get("/products/1")
    assert response.status_code == 200

def test_update_route(client):
    response = client.put("/products/1", json={"price": 900.0})
    assert response.status_code == 200

def test_delete_route(client):
    response = client.delete("/products/1")
    assert response.status_code == 204

def test_list_all_route(client):
    response = client.get("/products")
    assert response.status_code == 200

LIST BY NAME
CATEGORY
AVAILABILITY
