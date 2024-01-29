from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Engine, create_engine
from util.log import Log
from time import sleep
from models.user import Users 
from models.service import Services 

Base = declarative_base()


class DB:
    __engine__: Engine = None
    __session_func__ = None

    @classmethod
    def ensure_model_tables(cls):
        print("Creating tables")
        Users.__table__.create(bind=cls.get_engine(), checkfirst=True)
        Services.__table__.create(bind=cls.get_engine(), checkfirst=True)
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
