from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileField, FileRequired

class uploadForm(FlaskForm):
    imgurl=StringField()
    imgfile=FileField(validators=[FileRequired()])