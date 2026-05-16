from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, NumberRange


class BookForm(FlaskForm):

    title = StringField(
        'Название',
        validators=[DataRequired(), Length(max=100)]
    )
    author = StringField(
        'Автор',
        validators=[DataRequired(), Length(max=80)]
    )
    genre = StringField(
        'Жанр',
        validators=[DataRequired()]
    )
    year = IntegerField(
        'Год издания',
        validators=[Optional(), NumberRange(min=1000, max=2026)]
    )
    description = TextAreaField('Описание')
    cover_filename = StringField(
        'Имя файла обложки',
        validators=[Optional(), Length(max=100)]
    )
    submit = SubmitField('Добавить книгу')