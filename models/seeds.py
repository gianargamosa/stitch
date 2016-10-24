import settings
from middlewares import *

faker = Faker()
mysql = settings.mysql()

def seed_user():
  for x in xrange(1, 10):
    mysql.run("INSERT INTO users(username, fullname, email, password, biography, address) VALUES(%s, %s, %s, %s, %s, %s)", (faker.username(), faker.name(), faker.email(), faker.name(), faker.name(), faker.full_address()))

# def contact_faker():
#   for x in xrange(1, 100):
#     mysql.run("INSERT INTO users(username, fullname, email, password, biography, address) VALUES(%s, %s, %s, %s, %s, %s)", (faker.name(), faker.name(), faker.name(), faker.name(), faker.name(), faker.name()))