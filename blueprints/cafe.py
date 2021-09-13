from databases.models.tables.cafe import Cafe
from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from managers.cafe import add_cafe
CAFES_BLUEPRINT = Blueprint('cafes', __name__)


@CAFES_BLUEPRINT.route('', methods=['GET'])
def get_cafes():
    return {'m': 'get'}


@CAFES_BLUEPRINT.route('', methods=['POST'])
def create_cafe():
    return {'m': 'post'}


@CAFES_BLUEPRINT.route('', methods=['PUT'])
def update_cafe():
    return {'m': 'put'}


@CAFES_BLUEPRINT.route('', methods=['DELETE'])
def delete_cafe():
    return {'m': 'delete'}
