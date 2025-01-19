@app.route('/products/<int:id>', methods=['GET'])
def read_product(id):
    return jsonify(get_product_by_id(id)), 200

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    update_product_data(id, data)
    return '', 200

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    delete_product_by_id(id)
    return '', 204

@app.route('/products', methods=['GET'])
def list_products():
    # Add filters for name, category, availability
    pass
