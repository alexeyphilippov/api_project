import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')

    SQLALCHEMY_DATABASE_URL = 'postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}'.format(**{
        'host': os.getenv('DATABASE_HOST', 'localhost'),
        'port': os.getenv('DATABASE_PORT', '5432'),
        'database': os.getenv('DATABASE_NAME', 'api_db'),
        'user': os.getenv('DATABASE_USER', 'postgres'),
        'password': os.getenv('DATABASE_PASSWORD', 'postgres')
    })

    TIMEZONE = 'Europe/Moscow'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
