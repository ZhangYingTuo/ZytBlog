from datetime import datetime
from . import db

class Post(db.Model):
    """博客文章模型"""
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<Post {self.title}>'

class Comment(db.Model):
    """评论模型"""
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author = db.Column(db.String(100))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    
    def __repr__(self):
        return f'<Comment {self.id}>'
