from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    """文章表单"""
    title = StringField('标题', validators=[DataRequired(), Length(1, 200)])
    body = TextAreaField('内容', validators=[DataRequired()])
    author = StringField('作者', validators=[DataRequired(), Length(1, 100)])
    submit = SubmitField('发布')

class CommentForm(FlaskForm):
    """评论表单"""
    body = TextAreaField('评论内容', validators=[DataRequired()])
    author = StringField('姓名', validators=[DataRequired(), Length(1, 100)])
    submit = SubmitField('提交评论')
