import sqlite3
from .create_user_table import create_user_table
from .create_todo_table import create_todo_table
from .create_note_table import create_note_table
from .create_relations import create_relations

connection = sqlite3.connect('storage.db')

create_user_table(connection)
create_todo_table(connection)
create_note_table(connection)
create_relations(connection)
