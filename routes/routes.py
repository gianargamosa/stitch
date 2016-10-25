#!/usr/bin/env python
#coding:utf-8
from handlers import *
import tornado.web
import os

urls = [
  (r"/", crud_handler.CrudHandler),
  (r"/crud", crud_handler.CrudHandler),
  (r"/crud/new", crud_handler.CrudHandler),
  (r"/crud/edit", crud_handler.CrudHandler)
]