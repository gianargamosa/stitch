#!/usr/bin/env python
#coding:utf-8
from handlers import *

urls = [
  (ur"/", main_handler.MainHandler),
  (ur"/users", users_handler.UsersHandler),
  (ur"/users/new", users_handler.UsersHandler),
  (ur"/users/edit", users_handler.UsersHandler)
]
