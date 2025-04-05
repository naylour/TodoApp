from sqlite3 import Connection, Error

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
    except Error as error:
        print('[ USER ] Ошибка при обработке таблицы')
        print(error)
    finally:
        print('[ USER ] Успешная обработка таблицы')
