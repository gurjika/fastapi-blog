import psycopg2
from psycopg2.extras import RealDictCursor
import time



while True:
    try:
        conn = psycopg2.connect(
            host='localhost', 
            database='fastapis', 
            user='postgres', 
            password='password', 
            port='5431',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print('connected to postgres')
        break
    except Exception as e:
        print('{e}'.format(e))
        time.sleep(3)
