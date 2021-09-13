import random

from databases.models.tables.cafe import Cafe


def add_cafe():
    pass


def get_cafes_list():
    cafe_list = Cafe.get_cafes()
    return {'cafes': {cafe.id: cafe.to_dict() for cafe in cafe_list}}


def get_one_random_cafe():
    cafe_list = Cafe.get_cafes()
    random_cafe = random.choice(cafe_list)
    return random_cafe.to_dict()

def get_cafe_by_location(location):
    cafe_list =  Cafe.get_cafe_by_location(location).all()
    return {'cafes': {cafe.id: cafe.to_dict() for cafe in cafe_list}}

def update_cafe_details():
    pass


def delete_cafe_details():
    pass
