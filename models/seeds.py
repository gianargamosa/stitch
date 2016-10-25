from middlewares import *
import model_config

seed = Seeder()
mysql = model_config.mysql()

def seed_user():
  for x in xrange(1, 10):
    mysql.run("INSERT INTO users(username, fullname, email, password, biography, address) VALUES(%s, %s, %s, %s, %s, %s)", (seed.username(), seed.name(), seed.email(), seed.name(), seed.name(), seed.full_address()))

def seed_contact():
  for x in xrange(1, 100):
    mysql.run("INSERT INTO users(username, fullname, email, password, biography, address) VALUES(%s, %s, %s, %s, %s, %s)", (seed.name(), seed.name(), seed.name(), seed.name(), seed.name(), seed.name()))