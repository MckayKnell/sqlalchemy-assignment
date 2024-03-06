from flask import jsonify

from db import db
from models.products import Products
from models.categories import Categories


def product_add(req):
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
        return jsonify({'message': 'product created', 'result': values}), 201
    except:
        db.session.rollback()
        return jsonify({'message': 'unable to create record'}), 400


def product_add_category(req):
    post_data = req.form if req.form else req.json

    product_id = post_data.get('product_id')
    category_id = post_data.get('category_id')

    product_query = db.session.query(Products).filter(Products.product_id == product_id).first()
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    product_query.categories.append(category_query)
    db.session.commit()
    return jsonify({'message': 'category assigned to product', 'results': product_query})


def product_remove_category(req):
    post_data = req.form if req.form else req.json

    product_id = post_data.get('product_id')
    category_id = post_data.get('category_id')

    product_query = db.session.query(Products).filter(Products.product_id == product_id).first()
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    product_query.categories.remove(category_query)
    db.session.commit()
    return jsonify({'message': 'category assigned to product', 'results': product_query})


def products_get_all():
    query = db.session.query(Products).all()

    products_list = []

    for product in query:
        products_list.append({
            "product_id": product.product_id,
            "company_id": product.company_id,
            "products_name": product.product_name,
            "decription": product.description,
            "price": product.price,
            "active": product.active
        })
    return jsonify({"message": "products found", "results": products_list}), 200


def products_active():
    query = db.session.query(Products).filter(Products.active == True).all()

    if not query:
        return jsonify({"message": f'products could not be found'}), 404
    products_list = []

    for product in query:
        products_list.append({
            "product_id": product.product_id,
            "company_id": product.company_id,
            "products_name": product.product_name,
            "decription": product.description,
            "price": product.price,
            "active": product.active
        })
    return jsonify({"message": "products found", "results": products_list}), 200


def product_by_id(product_id):
    query = db.session.query(Products).filter(Products.product_id == product_id).all()

    if not query:
        return jsonify({"message": f'product could not be found'}), 404
    products_list = []

    for product in query:
        products_list.append({
            "product_id": product.product_id,
            "company_id": product.company_id,
            "products_name": product.product_name,
            "decription": product.description,
            "price": product.price,
            "active": product.active
        })
    return jsonify({"message": "products found", "results": products_list}), 200


def product_by_company_id(company_id):
    query = db.session.query(Products).filter(Products.company_id == company_id).all()

    if not query:
        return jsonify({"message": f'product could not be found'}), 404
    products_list = []

    for product in query:
        products_list.append({
            "product_id": product.product_id,
            "company_id": product.company_id,
            "products_name": product.product_name,
            "decription": product.description,
            "price": product.price,
            "active": product.active
        })
    return jsonify({"message": "products found", "results": products_list}), 200


def product_update(req, product_id):
    query = db.session.query(Products).filter(Products.product_id == product_id).first()
    post_data = req.form if req.form else req.get_json()

    query.product_id = post_data.get("product_id", query.product_id)
    query.product_name = post_data.get("product_name", query.product_name)
    query.description = post_data.get("description", query.description)
    query.price = post_data.get("price", query.price)
    query.active = post_data.get("active", query.active)

    try:
        db.session.commit()
        return jsonify({'message': 'product updated'}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400


def product_delete(req, product_id):
    query = db.session.query(Products).filter(Products.product_id == product_id).first()

    if not query:
        return jsonify({"message": 'product could not be found'}), 404

    try:
        db.session.delete(query)
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete product"})

    return jsonify({'message': 'record has been deleted'})
