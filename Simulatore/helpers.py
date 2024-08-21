from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField

class FormularioCER(FlaskForm):
    nome = StringField('Nome CER', [validators.DataRequired(), validators.Length(min=1, max=50)])
    provincia = StringField('Provincia', [validators.DataRequired(), validators.Length(min=1, max=30)])
    localita = StringField('Localita', [validators.DataRequired(), validators.Length(min=1, max=30)])
    indirizzo = StringField('Indirizzo', [validators.DataRequired(), validators.Length(min=1, max=50)])
    salvar = SubmitField('Salvar')

class FormularioUser(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=1, max=50)])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=1, max=50)])
    login = SubmitField('Login')