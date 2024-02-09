from flask import Blueprint, request
from controllers import companies_controller

companies = Blueprint('companies', __name__)


@companies.route('/companies', methods=['POST'])
def company_add():
    return companies_controller.company_add(request)
