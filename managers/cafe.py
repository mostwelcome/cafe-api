from databases.models.tables.cafe import Cafe

def add_cafe():
    pass

def get_cafes_list():
    return Cafe.get_cafe(1).to_dict()

def update_cafe_details():
    pass

def delete_cafe_details():
    pass