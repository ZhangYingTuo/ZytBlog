# ZytBlog

个人博客系统 - 记录一些灵感以及生活中的碎碎念

## 功能特性

- ✍️ 发布文章
- 💬 评论功能
- 📱 响应式设计
- 🔍 文章分页
- ✉️ 邮件通知

## 技术栈

- Flask 2.0.3
- SQLAlchemy (数据库ORM)
- Bootstrap 4 (前端框架)
- Flask-WTF (表单处理)
- Flask-Mail (邮件功能)

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/ZhangYingTuo/ZytBlog.git
cd ZytBlog
```

### 2. 创建虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 初始化数据库

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5. 运行应用

```bash
python manage.py
```

访问 http://localhost:5000 查看博客

## 环境变量配置

创建 `.env` 文件配置以下环境变量（可选）：

```
FLASK_CONFIG=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///data.sqlite
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-password
BLOG_ADMIN=admin@zytblog.com
```

## 运行测试

```bash
python manage.py test
```

或

```bash
python -m pytest tests/
```

## 项目结构

```
ZytBlog/
├── app/                    # 应用包
│   ├── main/              # 主蓝图
│   │   ├── __init__.py
│   │   ├── views.py       # 视图函数
│   │   ├── forms.py       # 表单类
│   │   └── errors.py      # 错误处理
│   ├── static/            # 静态文件
│   ├── templates/         # 模板文件
│   ├── __init__.py        # 应用工厂
│   ├── models.py          # 数据模型
│   └── email.py           # 邮件功能
├── tests/                 # 测试
├── config.py              # 配置文件
├── manage.py              # 启动脚本
└── requirements.txt       # 依赖包
```

## 开发指南

### 添加新文章

1. 访问首页，点击"写文章"
2. 填写文章标题、作者和内容
3. 点击"发布"

### 添加评论

1. 进入文章详情页
2. 在底部评论区填写姓名和评论内容
3. 点击"提交评论"

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License
