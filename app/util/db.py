from sqlalchemy import (Engine, create_engine, declarative_base) 
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