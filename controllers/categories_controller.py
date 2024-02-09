from flask import jsonify

from db import db
from models.category import Categories


def category_add(req):
    post_data = req.form if req.form else req.json

    fields = ['category_name']
    required_fields = ['category_name']

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data in required_fields and not field_data:
            return jsonify({'message': f'(field) is required'}), 400

        values[field] = field_data

    new_category = Categories(values['category_name'])

    try:
        db.session.add(new_category)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'message': 'unable to create record'}), 400

    query = db.session.query(Categories).filter(Categories.category_name == values['category_name']).first()

    values['category_id'] = query.category_id

    return jsonify({'message': 'category created', 'result': values}), 201


def category_update(req, category_id):
    query = db.session.query(Categories).filter(Categories.category_id == category_id).first()
    post_data = req.form if req.form else req.get_json()
    print(post_data)

    query.category_name = post_data.get("category_name", query.category_name)

    try:
        db.session.commit()
        return jsonify({'message': 'cateogory updated', 'results': {
            'category_id': query.category_id,
            'category_name': query.category_name
        }}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400
