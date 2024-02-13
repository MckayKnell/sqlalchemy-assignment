from flask import Blueprint, request
from controllers import companies_controller

companies = Blueprint('companies', __name__)


@companies.route('/companies', methods=['POST'])
def company_add(req):
    return companies_controller.company_add(req)


@companies.route('/companies', methods=['GET'])
def company_get():
    return companies_controller.company_get()


@companies.route('/companies/<company_id>', methods=['GET'])
def company_by_id(company_id):
    return companies_controller.company_by_id(company_id)


@companies.route('/companies/<company_id>', methods=['PUT'])
def company_update(req):
    return companies_controller.company_update(req)
