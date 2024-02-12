from flask import Blueprint, request
from controllers import companies_controller

companies = Blueprint('companies', __name__)


@companies.route('/companies', methods=['POST'])
def company_add(request):
    return companies_controller.company_add(request)


@companies.route('/companies', methods=['GET'])
def company_get():
    return companies_controller.company_get()


@companies.route('/companies', methods=['GET'])
def company_by_id(company_id):
    return companies_controller.company_by_id(company_id)


@companies.route('/companies', methods=['PUT'])
def company_update(request):
    return companies_controller.company_update(request)
