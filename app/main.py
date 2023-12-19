import sqlalchemy as db
from sqlalchemy.orm import declarative_base
import time

Base = declarative_base()

while True:
    try:
        engine = db.create_engine('postgresql+psycopg2://admin:fish123@psql/mydb')
        break
    except Exception:
        # while db spin up, may fail the first run before db created
        print("Failed to connect, trying again")
        time.sleep(1)

class Animals(Base):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

Animals.__table__.drop(bind=engine, checkfirst=True)
Animals.__table__.create(bind=engine)

ins = (
    db.insert(Animals).
    values(id = 1, name="test")
)
sel = db.select(Animals)

with engine.connect() as conn:
    conn.execute(ins)
    print(conn.execute(sel).fetchall())
