from flask import Blueprint, request
from controllers import products_controller

products = Blueprint('products', __name__)


@products.route('/products', methods=['POST'])
def product_add():
    return products_controller.product_add(request)


@products.route('/products', methods=['GET'])
def products_get():
    return products_controller.products_get()


@products.route('/products/active', methods=['GET'])
def products_active():
    return products_controller.products_active()


@products.route('/products/<product_id>', methods=['GET'])
def product_by_id(product_id):
    return products_controller.product_by_id(product_id)


@products.route('/products/<product_id>', methods=['PUT'])
def product_update(product_id):
    return products_controller.product_update(request, product_id)


@products.route('/products/<product_id>', methods=['DELETE'])
def product_delete(product_id):
    return products_controller.product_delete(request, product_id)
