from flask import Blueprint, request
from controllers import categories_controller

categories = Blueprint('categories', __name__)


@categories.route('/categories', methods=['POST'])
def category_add(request):
    return categories_controller.category_add(request)


@categories.route('/categories', methods=['GET'])
def category_get():
    return categories_controller.category_get()


@categories.route('/categories', methods=['GET'])
def category_by_id(category_id):
    return categories_controller.category_by_id(category_id)


@categories.route('/categories', methods=['PUT'])
def category_update(request):
    return categories_controller.category_update(request)
