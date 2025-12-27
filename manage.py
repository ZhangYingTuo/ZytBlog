import os
from app import create_app, db
from app.models import Post, Comment
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    """为Flask shell添加上下文"""
    return dict(db=db, Post=Post, Comment=Comment)

@app.cli.command()
def test():
    """运行单元测试"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    # WARNING: Debug mode should only be used for local development
    # Never run with debug=True in production environments
    # For production, use a proper WSGI server like Gunicorn or uWSGI
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode)
