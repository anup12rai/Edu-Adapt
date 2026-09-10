<<<<<<< HEAD
class Config:
    SECRET_KEY = "eduadapt_secret"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:@localhost:3306/eduadapt"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
=======
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-before-production')
    MYSQL_HOST = os.getenv('MYSQL_HOST', '127.0.0.1')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', '3306'))
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'eduadapt')
>>>>>>> 1650dd9 (eduadapt project)
