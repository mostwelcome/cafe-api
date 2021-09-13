from databases.db import db


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def __str__(self):
        return f'{self.name} -- {self.seats}'

    def to_dict(self):
        # Method 1.
        dictionary = {}
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    @classmethod
    def get_cafes(cls):
        return cls.query.all()

    @classmethod
    def get_cafe(cls, idx):
        return cls.query.get(idx)

    @classmethod
    def get_cafe_by_location(cls, loc):
        return cls.query.filter_by(location=loc)

    @classmethod
    def create_cafe(cls, **kwargs):
        cafe = cls(**kwargs)
        return cafe.save()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete_cafe(self):
        db.session.delete(self)
        db.session.commit()
        return self
