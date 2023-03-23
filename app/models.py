from app import db

 

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False )
    last_name = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(64))
    email = db.Column(db.String(64))
    notes = db.Column(db.String(64))
    def __repr__(self):
        return f"Address('{self.first_name}', '{self.last_name}', '{self.phone}', '{self.address}', '{self.email}', '{self.notes}')"
    


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()