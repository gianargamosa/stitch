## Synopsis

At the top of the file there should be a short introduction and/ or overview that explains **what** the project is. This description should match descriptions added for package managers (Gemspec, package.json, etc.)

## Code Example

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

from middlewares import *
from models import *
from routes import *

import tornado.ioloop
import tornado.web
import tornado.options
import sys
import os

# f = Faker()

# print f.name()

# user_model.select_user()

# seeds.seed_user()
# seeds.seed_contact()

settings = {
  "template_path" : os.path.join(os.path.dirname(__file__), "views"),
  "static_path" : os.path.join(os.path.dirname(__file__), "assets"),
  "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
  "xsrf_cookies": False,
}

def make_app():
  return tornado.web.Application(
    routes.urls,
    debug=True,
    **settings
  )

if __name__ == "__main__":
  app = make_app()
  app.listen(8888)
  tornado.options.parse_command_line()
  tornado.ioloop.IOLoop.instance().start()

## Motivation

A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Installation

Provide code examples and explanations of how to get the project.

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

Describe and show how to run the tests with code examples.

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

A short snippet describing the license (MIT, Apache, etc.)