import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password@localhost/fastapis'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# while True:
#     try:
#         conn = psycopg2.connect(
#             host='localhost', 
#             database='fastapis', 
#             user='postgres', 
#             password='password', 
#             port='5431',
#             cursor_factory=RealDictCursor
#         )
#         cursor = conn.cursor()
#         print('connected to postgres')
#         break
#     except Exception as e:
#         print('{e}'.format(e))
#         time.sleep(3)
