#!/usr/bin/env python
#coding:utf-8

import tornado.ioloop
import tornado.web

import routes
import sys
import os

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

# application = tornado.web.Application(urls.urls,**settings)

if __name__ == "__main__":
  app = make_app()
  app.listen(8000)
  tornado.ioloop.IOLoop.instance().start()
