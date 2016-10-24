#!/usr/bin/env python
#coding:utf-8

import MySQLdb
import database_conf
from base_handler import  BaseHandler

class UsersHandler(BaseHandler):

    def index(self):
        con = MySQLdb.connect(**database_conf.mysql)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("select * from user")
        users = cursor.fetchall()
        cursor.close()
        con.close()
        self.render('users/index.html',users=users)

    def post(self):
        print self.request
        name = self.get_argument('name',None)
        age = self.get_argument('age',None)
        con = MySQLdb.connect(**database_conf.mysql)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("insert into user (name,age) values ('%s',%s)" % (name,age) )
        cursor.execute("commit")
        cursor.close()
        con.close()
        self.redirect('/users')     

    def new(self):
        self.render('users/new.html')

    def edit(self):
        user_id = self.get_argument('id')
        con = MySQLdb.connect(**database_conf.mysql)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("select * from user where id=%s " % user_id)
        user = cursor.fetchone()
        cursor.close()
        con.close()
        self.render('users/edit.html',user=user)

    def put(self):
        user_id,name,age = self.get_argument('id'), self.get_argument('name'), self.get_argument('age')
        con = MySQLdb.connect(**database_conf.mysql)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("update user set name='%s', age=%s where id=%s" % (name,age,user_id))
        cursor.execute("commit")
        cursor.close()
        con.close()
        self.redirect('/users')     

    def delete(self):
        user_id = self.get_argument('id')
        con = MySQLdb.connect(**database_conf.mysql)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("delete from user where id=%s" % (user_id))
        cursor.execute("commit")
        cursor.close()
        con.close()
        self.redirect("/users")

