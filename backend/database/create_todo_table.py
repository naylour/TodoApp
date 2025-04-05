from sqlite3 import Connection, Error

def create_todo_table(connection: Connection):
    try:
        print('[ TODO ] Обработка таблицы')

        cursor = connection.cursor()

        cursor.execute('''--sql
            CREATE TABLE
            IF NOT EXISTS
            Todo (
                id TEXT NOT NULL PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                is_completed INTEGER
                updated_at TEXT NOT NULL
            );
        ''')

        connection.commit()
    except Error as error:
        print('[ TODO ] Ошибка при обработке таблицы')
        print(error)
    finally:
        print('[ TODO ] Успешная обработка таблицы')
