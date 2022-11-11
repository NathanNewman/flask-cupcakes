from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import InputRequired


class CupcakeForm(FlaskForm):
    """Form for adding cupcakes."""

    flavor = StringField("Flavor", validators=[InputRequired()])
    size = SelectField(
        "Size", choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])
    rating = IntegerField("Rating", validators=[InputRequired()])
    image = StringField("Image URL")
