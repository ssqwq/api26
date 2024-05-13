#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/23 10:48
# Author    : zhangqi
# @File     : db.py
# @Software : PyCharm
import pymysql
#取连接方法
def get_db_conn():
    conn = pymysql.connect(host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    db='p2p',
    charset='utf8mb4')#如果查询有中文，需要指定测试集编码
    return conn
#安装数据库查询操作
def query_db(sql):
    conn = get_db_conn()#获取连接
    cur = conn.cursor()#建立游标
    cur.execute(sql)#执行sql
    result = cur.fetchall()#获取所有查询结果
    cur.close()#关闭游标
    conn.close()#关闭连接
    return result#返回结果
#安装数据库查询操作
def change_db(sql):
    conn = get_db_conn()#获取连接
    cur = conn.cursor()#建立游标
    try:
        cur.execute(sql)#执行sql
        result = cur.fetchall()#获取所有查询结果
    except Exception as e:
        conn.rollback()#回滚
    finally:
        cur.close()#关闭游标
        conn.close()#关闭连接

# 安装数据库查询操作
def check_produck(num):
#注意sql中''号嵌套的问题
    sql = "SELECT * FROM product WHERE proNum='{}'".format(num)
    result = query_db(sql)
#三目运算符
    return True if result else False

def add_produck(num,name,limiti,annual):
    sql = "INSERT INTO produck(pronum,proname,prolimit,annualized) VALUE('{}','{}','{}','{}')".format(num,name,limiti,annual)
    change_db(sql)
def del_produck(num):
    sql = "delete from produck where pronum='{}'".format(num)
    change_db(sql)







