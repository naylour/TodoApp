from sqlite3 import Connection, Error

def create_relations(connection: Connection):
    try:
        print('[ RELATIONS ] Обработка таблицы')

        cursor = connection.cursor()

        cursor.execute('''--sql
            CREATE TABLE
            IF NOT EXISTS
            UserNote (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                note_id TEXT
            );
        ''')

        cursor.execute('''--sql
            CREATE TABLE
            IF NOT EXISTS
            UserTodo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                todo_id TEXT
            );
        ''')

        connection.commit()
    except Error as error:
        print('[ RELATIONS ] Ошибка при обработке таблицы')
        print(error)
    finally:
        print('[ RELATIONS ] Успешная обработка таблицы')
