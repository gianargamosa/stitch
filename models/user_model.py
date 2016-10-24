from middlewares import *
import model

mysql = model.mysql()
mysql.cache(60)

def user_model():
  return mysql.run_query("SELECT * FROM users")
    