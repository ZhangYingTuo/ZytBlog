from flask import render_template, redirect, url_for, flash, request
from . import main
from .. import db
from ..models import Post, Comment
from .forms import PostForm, CommentForm

@main.route('/')
def index():
    """首页 - 显示所有博客文章"""
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=10, error_out=False)
    posts = pagination.items
    return render_template('index.html', posts=posts, pagination=pagination)

@main.route('/post/<int:id>')
def post(id):
    """文章详情页"""
    post = Post.query.get_or_404(id)
    comments = Comment.query.filter_by(post_id=id).order_by(Comment.timestamp.asc()).all()
    form = CommentForm()
    return render_template('post.html', post=post, comments=comments, form=form)

@main.route('/post/new', methods=['GET', 'POST'])
def new_post():
    """创建新文章"""
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            body=form.body.data,
            author=form.author.data
        )
        db.session.add(post)
        db.session.commit()
        flash('文章发布成功！', 'success')
        return redirect(url_for('.index'))
    return render_template('new_post.html', form=form)

@main.route('/post/<int:id>/comment', methods=['POST'])
def add_comment(id):
    """添加评论"""
    post = Post.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            body=form.body.data,
            author=form.author.data,
            post_id=post.id
        )
        db.session.add(comment)
        db.session.commit()
        flash('评论添加成功！', 'success')
    return redirect(url_for('.post', id=post.id))
