import sqlite3
from faker import Faker
import random

DB_NAME = "task_manager.db"
fake = Faker()

def clear_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("pragma foreign_keys = on;")
    cur = conn.cursor()

    cur.execute("delete from tasks;")
    cur.execute("delete from users;")
    cur.execute("delete from status;")
    cur.execute("delete from sqlite_sequence;")

    conn.commit()
    conn.close()
    print("Database cleared and autoincrement reset.")

def seed_statuses():
    statuses = [
        ("new",),
        ("in progress",),
        ("completed",),
    ]

    conn = sqlite3.connect(DB_NAME)
    conn.execute("pragma foreign_keys = on;")
    cur = conn.cursor()

    cur.execute("delete from status;")

    cur.executemany(
        "insert into status (name) values (?);",
        statuses
    )

    conn.commit()
    conn.close()
    print("Statuses seeded successfully.")

def seed_users(n: int = 10):
    conn = sqlite3.connect(DB_NAME)
    conn.execute("pragma foreign_keys = on;")
    cur = conn.cursor()

    cur.execute("delete from users;")

    users = []
    for _ in range(n):
        fullname = fake.name()
        email = fake.unique.email()
        users.append((fullname, email))

    cur.executemany(
        "insert into users (fullname, email) values (?, ?);",
        users
    )

    conn.commit()
    conn.close()
    print(f"{n} users seeded successfully.")

def seed_tasks(n: int = 30):
    conn = sqlite3.connect(DB_NAME)
    conn.execute("pragma foreign_keys = on;")
    cur = conn.cursor()

    cur.execute("delete from tasks;")

    cur.execute("select id from status;")
    status_ids = [row[0] for row in cur.fetchall()]

    cur.execute("select id from users;")
    user_ids = [row[0] for row in cur.fetchall()]

    tasks = []
    for _ in range(n):
        title = fake.sentence(nb_words=4)
        description = fake.text(max_nb_chars=100)
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        tasks.append((title, description, status_id, user_id))

    cur.executemany(
        "insert into tasks (title, description, status_id, user_id) values (?, ?, ?, ?);",
        tasks
    )

    conn.commit()
    conn.close()
    print(f"{n} tasks seeded successfully.")

if __name__ == "__main__":
    clear_db()
    seed_statuses()
    seed_users(10)
    seed_tasks(30)