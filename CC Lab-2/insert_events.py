from database import get_db

db = get_db()

# create table if not exists
db.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    fee INTEGER
)
""")

events = [
    ("Hackathon", 500),
    ("Dance Battle", 300),
    ("AI Workshop", 400),
    ("Photography Walk", 200),
    ("Gaming Tournament", 350),
    ("Music Night", 250),
    ("Treasure Hunt", 150),
    ("Stand-up Comedy", 300),
    ("Robo Race", 450),
]

for e in events:
    db.execute("INSERT INTO events (name, fee) VALUES (?, ?)", e)

db.commit()
db.close()

print("✅ Events inserted successfully!")
