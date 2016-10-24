#!/usr/bin/env python
#coding:utf-8

from base_handler import  BaseHandler
from models import *

class MainHandler(BaseHandler):

  def index(self):
    users = user_model.select_user()
    self.render('main/index.html', users=users)

  def post(self):
    self.redirect('/')

  def new(self):
    self.render('main/new.html')

  def edit(self):
    print 'edit'
    self.render('main/edit.html')

  def put(self):
    user_id = self.get_argument('id')
    name = self.get_argument('name')
    age = self.get_argument('age')
    print user_id, name, age
    print update
    self.redirect('/')

  def delete(self):
    user_id = self.get_argument('id')
    print 'delete', user_id
    self.redirect('/')



