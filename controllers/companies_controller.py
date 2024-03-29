from flask import jsonify

from db import db
from models.companies import Companies


def company_add(req):
    post_data = req.form if req.form else req.json

    fields = ['company_name']
    required_fields = ['company_name']

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data in required_fields and not field_data:
            return jsonify({'message': f'(field) is required'}), 400

        values[field] = field_data

    new_company = Companies(values['company_name'])
    try:
        db.session.add(new_company)
        db.session.commit()
        query = db.session.query(Companies).filter(Companies.company_name == values['company_name']).first()
        values['company_id'] = query.company_id
        return jsonify({'message': 'company created', 'result': values}), 201
    except:
        db.session.rollback()
        return jsonify({'message': 'unable to create record'}), 400


def companies_get_all():
    query = db.session.query(Companies).all()

    companies_list = []

    for company in query:
        companies_list.append({
            "company_id": company.company_id,
            "company_name": company.company_name,
        })
    return jsonify({"message": "companies found", "results": companies_list}), 200


def company_by_id(company_id):
    query = db.session.query(Companies).filter(Companies.company_id == company_id).all()

    if not query:
        return jsonify({"message": f'company could not be found'}), 404
    companies_list = []

    for company in query:
        companies_list.append({
            "company_id": company.company_id,
            "companies_name": company.company_name
        })
    return jsonify({"message": "company found", "results": companies_list}), 200


def company_update(req, company_id):
    post_data = req.form if req.form else req.json
    query = db.session.query(Companies).filter(Companies.company_id == company_id).first()

    query.company_name = post_data.get("company_name", query.company_name)

    try:
        db.session.commit()
        return jsonify({'message': 'company updated'}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400
