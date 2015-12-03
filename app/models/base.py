# -*- Encoding: utf-8 -*-
"""
app 初始化, db.create_all() 与 model 声明时, 都需要 db 变量.
如果在 __init__ 中声明 db, 容易形成循环 import
所以, 在单独的 base 文件中 declare
"""
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()
