from flask import Blueprint, request
from controllers import products_controller

products = Blueprint('products', __name__)


@products.route('/products', methods=['POST'])
def products_add(req):
    return products_controller.products_add(req)


@products.route('/products', methods=['GET'])
def products_get():
    return products_controller.products_get()


@products.route('/products/active', methods=['GET'])
def products_active():
    return products_controller.products_active()


@products.route('/products/<product_id>', methods=['GET'])
def products_by_id(product_id):
    return products_controller.products_by_id(product_id)


@products.route('/products/product_id', methods=['PUT'])
def products_update(req):
    return products_controller.products_update(req)


@products.route('/products/product_id', methods=['DELETE'])
def product_delete(product_id):
    return products_controller.product_delete(product_id)
