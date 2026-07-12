import sqlite3

# Database connect
conn = sqlite3.connect("disaster.db")

# Cursor create
cursor = conn.cursor()

# User Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Disaster Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS disasters(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    disaster_type TEXT NOT NULL,
    location TEXT NOT NULL,
    severity TEXT NOT NULL,
    description TEXT NOT NULL
)
""")

import sqlite3

conn = sqlite3.connect("disaster.db")
cursor = conn.cursor()

# User Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Disaster Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS disasters(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    disaster_type TEXT NOT NULL,
    location TEXT NOT NULL,
    severity TEXT NOT NULL,
    description TEXT NOT NULL
)
""")

# 👇 Drone Table (INGA ADD PANNUNGA)
cursor.execute("""
CREATE TABLE IF NOT EXISTS drones(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drone_name TEXT,
    model TEXT,
    status TEXT,
    battery INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS rescue_team(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT,
    leader TEXT,
    contact TEXT,
    location TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS drone_assignment(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drone_name TEXT,
    disaster_type TEXT,
    location TEXT,
    status TEXT
)
""")

import sqlite3

conn = sqlite3.connect("disaster.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS drones(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drone_name TEXT,
    drone_type TEXT,
    location TEXT,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS assignments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    disaster_id INTEGER,
    drone_id INTEGER,
    assigned_date TEXT
)
""")

conn.commit()
conn.close()

print("Database and Tables Created Successfully!")