from dotenv import load_dotenv
from os import getenv
load_dotenv()

MYSQL_HOST = 'localhost'
MYSQL_USER = getenv('MYSQL_USER')
MYSQL_PASSWORD = getenv('MYSQL_PASSWORD')
MYSQL_DB = getenv('MYSQL_DB')
MYSQL_CURSORCLASS = 'DictCursor'
SECRET_KEY = getenv('SECRET_KEY') 
