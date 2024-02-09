from flask import jsonify

from db import db
from models.products import Products


def products_add(req):
    post_data = req.form if req.form else req.json

    fields = ['product_name', 'price', 'description', 'company_id']
    required_fields = ['product_name', 'price', 'description', 'company_id']

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data in required_fields and not field_data:
            return jsonify({'message': f'(field) is required'}), 400

        values[field] = field_data

    new_products = Products(**values)

    try:
        db.session.add(new_products)
        db.session.commit()
        query = db.session.query(Products).filter(Products.product_name == values['product_name']).first()
        values['product_id'] = query.product_id
        return jsonify({'message': 'products created', 'result': values}), 201
    except:
        db.session.rollback()
        return jsonify({'message': 'unable to create record'}), 400


def products_update(req, product_id):
    query = db.session.query(Products).filter(Products.product_id == product_id).first()
    post_data = req.form if req.form else req.get_json()
    print(post_data)

    query.product_id = post_data.get("product_id", query.product_id)
    query.product_name = post_data.get("product_name", query.product_name)
    query.description = post_data.get("description", query.description)
    query.price = post_data.get("price", query.price)
    query.active = post_data.get("active", query.active)

    try:
        db.session.commit()
        return jsonify({'message': 'product updated', 'results': {
            'product_id': query.product_id,
            'product_name': query.product_name,
            'description': query.description,
            'price': query.price,
            'active': query.active
        }}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400

    # return jsonify({"message": 'product updated', "results": query}), 200
