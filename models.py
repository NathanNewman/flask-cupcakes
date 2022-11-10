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

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)