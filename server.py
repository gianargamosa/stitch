#!/usr/bin/env python
#coding:utf-8

from middlewares import *
from models import *

import tornado.ioloop
import tornado.web
import tornado.options

import routes
import sys
import os

# user_model.user_model()

# seeds.user_faker()
# seeds.contact_faker()
# print names

settings = {
  "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
  "static_path" : os.path.join(os.path.dirname(__file__), "assets"),
  "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
  "xsrf_cookies": False,
}

def make_app():
  return tornado.web.Application(
    routes.urls,
    **settings
  )

if __name__ == "__main__":
  app = make_app()
  app.listen(8000)
  tornado.options.parse_command_line()
  tornado.ioloop.IOLoop.instance().start()
