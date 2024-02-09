from flask import Blueprint, request
from controllers import product_category_xref

xref = Blueprint('products/categories', __name__)


@xref.route('/products/categories', methods=['POST'])
def products_category_xref_add():
    return product_category_xref.product_category_xref_add(request)
