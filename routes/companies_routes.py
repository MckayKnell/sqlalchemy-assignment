from flask import Blueprint, request
from controllers import companies_controller

companies = Blueprint('companies', __name__)


@companies.route('/companies', methods=['POST'])
def company_add():
    return companies_controller.company_add(request)


@companies.route('/companies', methods=['GET'])
def companies_get():
    return companies_controller.companies_get()


@companies.route('/companies/<company_id>', methods=['GET'])
def company_by_id(company_id):
    return companies_controller.company_by_id(company_id)


@companies.route('/companies/<company_id>', methods=['PUT'])
def company_update(company_id):
    return companies_controller.company_update(request, company_id)
