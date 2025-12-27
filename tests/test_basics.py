import unittest
from flask import current_app
from app import create_app, db

class BasicsTestCase(unittest.TestCase):
    """基础测试用例"""
    
    def setUp(self):
        """每个测试前的设置"""
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
    
    def tearDown(self):
        """每个测试后的清理"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_app_exists(self):
        """测试应用实例是否存在"""
        self.assertIsNotNone(current_app)
    
    def test_app_is_testing(self):
        """测试应用是否在测试模式"""
        self.assertTrue(current_app.config['TESTING'])
    
    def test_home_page(self):
        """测试首页"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ZytBlog', response.data)

if __name__ == '__main__':
    unittest.main()
