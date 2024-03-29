# pip install fastapi_users

# With SQLAlchemy support
# pip install 'fastapi-users[sqlalchemy]'

# With Beanie support
# pip install 'fastapi-users[beanie]'

# Asynchronous driver
# pip install asyncpg     # For PostgreSQL
# pip install aiosqlite   # For SQLite: 

# Examples of DB_URLs are:
# engine = create_engine('postgresql+asyncpg://user:password@host:port/name') # PostgreSQL
# engine = create_engine('sqlite+aiosqlite:///name.db')                       # SQLite



# V1 - выход полтзователя из системы не удаляет сразу TOKEN


import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="localhost", log_level="info")