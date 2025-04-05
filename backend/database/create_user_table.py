from sqlite3 import Connection, Error
from datetime import datetime
from ulid import ULID
from argon2 import PasswordHasher

hasher = PasswordHasher()

def create_user_table(connection: Connection):
    try:
        print('[ USER ] Обработка таблицы')

        cursor = connection.cursor()

        cursor.execute('''--sql
            CREATE TABLE
            IF NOT EXISTS
            User (
                id TEXT NOT NULL PRIMARY KEY,
                last_name TEXT,
                first_name TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT,
                updated_at TEXT NOT NULL
            );
        ''')


        connection.commit()

        # res = cursor.execute(f'''
        #     INSERT INTO User (id, last_name, first_name, username, password, updated_at)
        #     VALUES (?, ?, ?, ?, ?, ?) RETURNING changes();
        # ''', (str(ULID()), None, 'bb', 'ggd', hasher.hash('datapassword'), datetime.now()))

        # print(res.fetchall())
    except Error as error:
        print('[ USER ] Ошибка при обработке таблицы')
        print(error)
    finally:
        print('[ USER ] Успешная обработка таблицы')
