from sqlalchemy.orm import declarative_base
from sqlalchemy import (Engine, create_engine) 
from util.log import Log 
from time import sleep

Base = declarative_base()


class DB:
    __engine__: Engine = None
    
    @classmethod
    def get_engine(cls):
        if cls.__engine__ is None:

            cls.__engine__ = create_engine('postgresql+psycopg2://admin:fish123@psql/mydb')

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