from wtforms import SelectField, StringField, FloatField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Optional, URL


class CupcakesForm(FlaskForm):
    """Form for adding playlists."""


    flavor = StringField(
        "Flavor",
        validators=[InputRequired()]
    )

    size = StringField(
        "Size",
        validators=[InputRequired()]
    )

    rating = FloatField(
        "Rating",
        validators=[InputRequired()]
    )

    image = StringField(
        "Image URL",
        validators=[Optional(), URL]
    )