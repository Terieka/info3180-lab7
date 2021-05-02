from flask_wtf import FlaskForm
from wtforms import TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired

  
class UploadForm(FlaskForm):
    descriptiom = TextAreaField("Description", [validators.required()])
    photo = FileField('Image', validators=[FileRequired(),FileAllowed(['jpg','png'], 'Please Upload Images Only!')])
