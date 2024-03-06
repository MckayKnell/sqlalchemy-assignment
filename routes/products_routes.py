from flask import Blueprint, request
from controllers import products_controller

products = Blueprint('products', __name__)


@products.route('/products', methods=['POST'])
def product_add():
    return products_controller.product_add(request)


@products.route('/product/category', methods=['POST'])
def product_add_category():
    return products_controller.product_add_category(request)


@products.route('/products', methods=['GET'])
def products_get_all():
    return products_controller.products_get_all()


@products.route('/products/active', methods=['GET'])
def products_active():
    return products_controller.products_active()


@products.route('/product/<product_id>', methods=['GET'])
def product_by_id(product_id):
    return products_controller.product_by_id(product_id)


@products.route('/products/<company_id>', methods=['GET'])
def product_by_company_id(company_id):
    return products_controller.product_by_company_id(company_id)


@products.route('/product/<product_id>', methods=['PUT'])
def product_update(product_id):
    return products_controller.product_update(request, product_id)


@products.route('/product/category', methods=['DELETE'])
def product_remove_category():
    return products_controller.product_remove_category(request)


@products.route('/products/<product_id>', methods=['DELETE'])
def product_delete(product_id):
    return products_controller.product_delete(request, product_id)
