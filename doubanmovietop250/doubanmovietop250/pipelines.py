# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql,time,logging

from doubanmovietop250 import settings
from doubanmovietop250.items import Doubanmovietop250Item

class Doubanmovietop250Pipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

        # 如果数据表已经存在使用 execute() 方法删除表。
        self.cursor.execute("DROP TABLE IF EXISTS top250")
        time.sleep(3)
        # 新建相关数据库表&字段
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS top250(
          ranking INT (6)  NOT NULL COMMENT '排名' ,
          movie_name VARCHAR (200)  CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '电影名称',
          score FLOAT (2,1)  DEFAULT NULL COMMENT '评分',
          score_num INT (10)  DEFAULT NULL COMMENT '评价人数',
          PRIMARY KEY(ranking))
          ''')
        # 设置超时时间3秒
        time.sleep(3)
    def process_item(self, item, spider):
        # 将items的信息存入数据库
        self.cursor.execute(
            """insert into top250(ranking,movie_name,score,score_num)
              value (%s,%s,%s,%s)""",
            (item['ranking'],
             item['movie_name'],
             item['score'],
             item['score_num']))
        # 提交sql语句
        self.connect.commit()