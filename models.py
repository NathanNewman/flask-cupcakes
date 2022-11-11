"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cupcake(db.Model):
    """Cupcake"""

    __tablename__ = "cupcakes"

    def __repr__(self):
        c = self
        return f"<Cupcake {c.id} flavor: {c.flavor} size: {c.size} rating: {c.rating}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    image = db.Column(db.Text, nullable=False,
                      default='https://tinyurl.com/demo-cupcake')

    def serialize(self):
        return {
            'id' : self.id,
            'flavor' : self.flavor,
            'size' : self.size,
            'rating' : self.rating,
            'image' : self.image
        }
    
    def submit_cupcake(self, form):
        flavor = form.flavor.data
        size = form.size.data
        rating = form.rating.data
        image = form.image.data
        cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
        db.session.add(cupcake)
        return db.session.commit()

    def edit_cupcake(self, Id, form):
        cupcake = Cupcake.query.get(Id)
        cupcake.flavor = form.flavor.data
        cupcake.size = form.size.data
        cupcake.rating = form.rating.data
        cupcake.image = form.image.data
        return db.session.commit()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)