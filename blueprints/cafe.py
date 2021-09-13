from databases.models.tables.cafe import Cafe
from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from managers.cafe import get_cafes_list, get_one_random_cafe, get_cafe_by_location, add_cafe, update_cafe_coffee_price, \
    delete_cafe_details

CAFES_BLUEPRINT = Blueprint('cafes', __name__)


@CAFES_BLUEPRINT.route('', methods=['GET'])
def get_cafes():
    return get_cafes_list()


@CAFES_BLUEPRINT.route('/random', methods=['GET'])
def get_random_cafe():
    return get_one_random_cafe()


@CAFES_BLUEPRINT.route('/search', methods=['GET'])
def search_cafe():
    location = request.args.get('location')
    return get_cafe_by_location(location)


@CAFES_BLUEPRINT.route('', methods=['POST'])
def create_cafe():
    cafe_details = Cafe(**request.get_json())
    return add_cafe(cafe_details)


@CAFES_BLUEPRINT.route('/update-price/<int:id>')
@CAFES_BLUEPRINT.route('/<int:idx>', methods=['PATCH'])
def update_price(idx=None):
    new_price = request.args.get('price')
    print(new_price)
    print(idx)
    return update_cafe_coffee_price(idx, new_price)


@CAFES_BLUEPRINT.route('/<int:idx>', methods=['DELETE'])
def delete_cafe(idx=None):
    return delete_cafe_details(idx)
