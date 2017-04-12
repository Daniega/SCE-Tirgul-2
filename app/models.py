from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), index=True, unique=False)
    last_name = db.Column(db.String(120), index=True, unique=False)
    id_number = db.Column(db.String(9), index=True, unique=False)
    voted = db.Column(db.Boolean, unique = False, default=False)

    def __init__(self, first_name, last_name, id_number, voted=False):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.voted = voted

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def user_voted(self):
        return True

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % self.first_name


class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=False)
    picture = db.Column(db.String(120), index=True, unique=False)
    vote_count = db.Column(db.Integer, index=True, unique=False)

    def __init__(self, name, picture, vote_count = 0):
        self.name = name
        self.picture = picture
        self.vote_count = vote_count

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<Party %r>' % self.name
