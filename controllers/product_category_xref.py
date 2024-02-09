from flask import jsonify

from db import db
from models.product_category_xref import products_categories_association_table


def product_category_xref_add(req):
    post_data = req.form if req.form else req.json

    fields = ['product_id', 'category_id']
    required_fields = ['product_id', 'category_id']

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data in required_fields and not field_data:
            return jsonify({'message': f'(field) is required'}), 400

        values[field] = field_data

    try:
        db.session.execute(products_categories_association_table.insert().values(values))
        db.session.commit()
        return jsonify({'message': 'association created', 'results': values}), 201
    except:
        db.session.rollback()
        return jsonify({'message': 'unable to create record'}), 400


# def product_category_xref_update(req, product_id, category_id):
#     query = db.session.query(Categories).filter(Categories.category_id == category_id).first()
#     post_data = req.form if req.form else req.get_json()
#     print(post_data)

#     query.category_name = post_data.get("category_name", query.category_name)

#     try:
#         db.session.commit()
#         return jsonify({'message': 'cateogory updated', 'results': {
#             'category_id': query.category_id,
#             'category_name': query.category_name
#         }}), 200
#     except:
#         db.session.rollback()
#         return jsonify({"message": "unable to update record"}), 400
