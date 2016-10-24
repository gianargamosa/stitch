import model
from faker import Faker

faker = Faker()
mysql = model.mysql()

def user_faker():
  for x in xrange(1, 10):
    mysql.run("INSERT INTO users(username, fullname, email, password, biography, address) VALUES(%s, %s, %s, %s, %s, %s)", (faker.name(), faker.name(), faker.name(), faker.name(), faker.name(), faker.name()))

def contact_faker():
  for x in xrange(1, 100):
    mysql.run("INSERT INTO users(username, fullname, email, password, biography, address) VALUES(%s, %s, %s, %s, %s, %s)", (faker.name(), faker.name(), faker.name(), faker.name(), faker.name(), faker.name()))