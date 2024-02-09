from flask import Blueprint, request
from controllers import products_controller

products = Blueprint('products', __name__)


@products.route('/products', methods=['POST'])
def products_add():
    return products_controller.products_add(request)


# @products.route('/products', methods=['POST'])
# def add_product():
#     return products_controller.add_product()
