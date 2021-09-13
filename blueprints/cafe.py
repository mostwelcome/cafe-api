from databases.models.tables.cafe import Cafe
from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from managers.cafe import get_cafes_list, get_one_random_cafe, get_cafe_by_location

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
    return {'m': 'post'}



@CAFES_BLUEPRINT.route('', methods=['PUT'])
def update_cafe():
    return {'m': 'put'}


@CAFES_BLUEPRINT.route('', methods=['DELETE'])
def delete_cafe():
    return {'m': 'delete'}
