from flask import Blueprint, request
from controllers import categories_controller

categories = Blueprint('categories', __name__)


@categories.route('/categories', methods=['POST'])
def category_add():
    return categories_controller.category_add(request)


# @categories.route('/categories', methods=['PUT'])
# def category_add():
#     return categories_controller.category_add(request)
