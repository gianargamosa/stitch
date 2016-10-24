#!/usr/bin/env python
#coding:utf-8
from handlers import *

urls = [
  (ur"/", MainHandler),
  (ur"/users", UsersHandler),
  (ur"/users/new", UsersHandler),
  (ur"/users/edit", UsersHandler)
]
