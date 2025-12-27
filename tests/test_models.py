import unittest
from datetime import datetime
from app import create_app, db
from app.models import Post, Comment

class ModelTestCase(unittest.TestCase):
    """数据模型测试用例"""
    
    def setUp(self):
        """每个测试前的设置"""
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        """每个测试后的清理"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_post_creation(self):
        """测试文章创建"""
        post = Post(title='测试文章', body='这是测试内容', author='测试作者')
        db.session.add(post)
        db.session.commit()
        self.assertIsNotNone(post.id)
        self.assertEqual(post.title, '测试文章')
    
    def test_comment_creation(self):
        """测试评论创建"""
        post = Post(title='测试文章', body='测试内容', author='作者')
        db.session.add(post)
        db.session.commit()
        
        comment = Comment(body='测试评论', author='评论者', post_id=post.id)
        db.session.add(comment)
        db.session.commit()
        self.assertIsNotNone(comment.id)
        self.assertEqual(comment.post_id, post.id)

if __name__ == '__main__':
    unittest.main()
