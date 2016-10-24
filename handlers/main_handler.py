#!/usr/bin/env python
#coding:utf-8

#!/usr/bin/env python
#coding:utf-8

from base_handler import  BaseHandler
from models import *

class MainHandler(BaseHandler):
    def get(self):
      users = user_model.select_user()
      self.render('index.html', users=users)



