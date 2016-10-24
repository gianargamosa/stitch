#!/usr/bin/env python
#coding:utf-8

import tornado
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def current_user(self):
        return 'user'

    def get(self):
        method = self.get_argument("method",None)
        if method == 'new':
            return self.new()
        elif method == 'edit':
            return self.edit()
        else:
            return self.index()

    def post(self):
        method = self.get_argument("method",None)
        if method == "put":
            return self.put()
        else:
            pass

    def put(self):
        pass

