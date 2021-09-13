import random

from databases.models.tables.cafe import Cafe


def add_cafe(cafe_obj):
    return Cafe.create_cafe(name=cafe_obj.name, map_url=cafe_obj.map_url, location=cafe_obj.location,
                            seats=cafe_obj.seats, img_url=cafe_obj.img_url,
                            has_toilet=cafe_obj.has_toilet, has_wifi=cafe_obj.has_wifi,
                            has_sockets=cafe_obj.has_sockets, can_take_calls=cafe_obj.can_take_calls).to_dict()


def get_cafes_list():
    cafe_list = Cafe.get_cafes()
    return {'cafes': {cafe.id: cafe.to_dict() for cafe in cafe_list}}

def update_cafe_coffee_price(idx,new_price):
    old_cafe = Cafe.get_cafe(idx)
    old_cafe.coffee_price = new_price
    return old_cafe.save().to_dict()


def get_one_random_cafe():
    cafe_list = Cafe.get_cafes()
    random_cafe = random.choice(cafe_list)
    return random_cafe.to_dict()


def get_cafe_by_location(location):
    cafe_list = Cafe.get_cafe_by_location(location).all()
    return {'cafes': {cafe.id: cafe.to_dict() for cafe in cafe_list}}


def update_cafe_details():
    pass


def delete_cafe_details():
    pass
