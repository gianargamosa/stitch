from middlewares import *
import settings

mysql = settings.mysql()
mysql.cache(60)

def select_user():
  return mysql.run_query("SELECT * FROM users")
    