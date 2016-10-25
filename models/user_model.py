from middlewares import *
import model_config

mysql = model_config.mysql()
mysql.cache(60)

def select_user():
  return mysql.run_query("SELECT * FROM users")
    