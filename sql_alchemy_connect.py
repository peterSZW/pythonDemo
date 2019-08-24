#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import threading

 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy import pool
from sqlalchemy.sql import text
from sqlalchemy.engine.result import ResultProxy

 
 
sqllink="mysql://root:123456@127.0.0.1:3306/mysql"

engine = create_engine(sqllink, max_overflow=5, pool_size=10,  pool_timeout=30)
Session = sessionmaker(bind=engine)

session = Session()

# 查询
cursor = session.execute('select * from db')
result = cursor.fetchall()
print(engine.pool.status())

# 添加
#cursor = session.execute('insert into users(name) values(:value)',params={"value":'hc'})
# 注意占位符和传参的形式
#session.commit()
print(cursor.lastrowid)
 

print(engine.pool.status())

session.close()
