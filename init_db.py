import sqlite3

DB_NAME = "task_manager.db"
SCHEMA_FILE = "schema.sql"


def init_db():
    with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        schema = f.read()

    conn = sqlite3.connect(DB_NAME)

    conn.execute("pragma foreign_keys = on;")

    conn.executescript(schema)
    conn.commit()
    conn.close()

    print("Database initialized successfully.")


if __name__ == "__main__":
    init_db()