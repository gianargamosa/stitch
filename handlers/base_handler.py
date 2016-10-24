#!/usr/bin/env python
#coding:utf-8

import tornado
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler,self).__init__(application,request)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('../public/errors/404.html', page=None)
        elif status_code == 500:
            self.render('../public/errors/500.html', page=None)
        else:
            self.render('../public/errors/unknown.html', page=None)

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

