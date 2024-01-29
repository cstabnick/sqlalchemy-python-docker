from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Engine, create_engine
from util.log import Log
from time import sleep
from models.user import Users 

Base = declarative_base()


class DB:
    __engine__: Engine = None
    __session_func__: sessionmaker() = None

    @classmethod
    def ensure_model_tables(cls):
        print("doing tables")
        Users.__table__.create(bind=cls.get_engine(), checkfirst=True)
        return 
        
    @classmethod
    def get_session(cls):
        return cls.__session_func__()

    @classmethod
    def get_engine(cls):
        if cls.__engine__ is None:
            cls.__engine__ = create_engine(
                "postgresql+psycopg2://admin:fish123@psql/mydb"
            )
            cls.__session_func__ = sessionmaker(cls.__engine__)
            # test connection
            while True:
                try:
                    cls.__engine__.connect()
                    Log.info("Connected!")
                    break

                except Exception as ex:
                    Log.exception(ex)
                    sleep(1)
            

        return cls.__engine__

    @classmethod
    def select_many(cls, select_statement):
        with cls.get_engine().connect() as conn:
            return conn.execute(select_statement).fetchall()

    @classmethod
    def insert_one(cls, insert_statement):
        with cls.get_engine().connect() as conn:
            conn.execute(insert_statement)
            conn.commit()

    @classmethod
    def insert_many(cls, insert_statements):
        with cls.get_engine().connect() as conn:
            for insert_statement in insert_statements:
                conn.execute(insert_statement)
            conn.commit()
