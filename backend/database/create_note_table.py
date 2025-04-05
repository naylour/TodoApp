from sqlite3 import Connection, Error

def create_note_table(connection: Connection):
    try:
        print('[ NOTE ] Обработка таблицы')

        cursor = connection.cursor()

        cursor.execute('''--sql
            CREATE TABLE
            IF NOT EXISTS
            Note (
                id TEXT NOT NULL PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT,
                updated_at TEXT NOT NULL
            );
        ''')

        connection.commit()
    except Error as error:
        print('[ NOTE ] Ошибка при обработке таблицы')
        print(error)
    finally:
        print('[ NOTE ] Успешная обработка таблицы')
