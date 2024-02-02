from typing import Dict, NamedTuple
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Engine, create_engine
from util.log import Log
from time import sleep
from models.user import Users 
from models.service import Services 
from util.constants import C_DEFAULT_CONNECTION_STRING

Base = declarative_base()

class DBEngineRecord(NamedTuple):
    engine: Engine
    session_mkr: sessionmaker

class DB:
    __engines__: Dict[str, DBEngineRecord] = {}

    @classmethod
    def ensure_model_tables(cls):
        print("Creating tables")
        Users.__table__.create(bind=cls.get_engine(), checkfirst=True)
        Services.__table__.create(bind=cls.get_engine(), checkfirst=True)
        return 
        
    @staticmethod
    def _get_dict_key(connection_str: str, connect_args: dict) -> str:
        return f"{connection_str}{connect_args}"

    @classmethod
    def _ensure_db_engine(cls, connection_str: str, connect_args: dict):
        key = cls._get_dict_key(connection_str=connection_str, connect_args=connect_args)
        if cls.__engines__.get(key) is None:
            engine = create_engine(
                url=connection_str,
                connect_args=connect_args
            )

            # test connection
            while True:
                try:
                    engine.connect()
                    Log.info("Connected!")
                    break

                except Exception as ex:
                    Log.exception(ex)
                    sleep(1)
            
            cls.__engines__[key] = DBEngineRecord(engine=engine, session_mkr=sessionmaker(bind=engine))

    @classmethod
    def get_session(cls, connection_str: str = C_DEFAULT_CONNECTION_STRING, connect_args: dict = {}) -> Session:
        """
        Gets a new session 

        Returns: SQLAlchemy Session object
        """
        cls._ensure_db_engine(connection_str=connection_str, connect_args=connect_args)
        session_mkr = cls.__engines__[cls._get_dict_key(connection_str=connection_str, connect_args=connect_args)].session_mkr
        return session_mkr()

    @classmethod
    def get_engine(cls, connection_str: str = C_DEFAULT_CONNECTION_STRING, connect_args: dict = {}) -> Engine:
        """
        Gets a sqlalchemy engine for a given connection string and connection args. If a match does not exist, a new engine is created.
        """
        cls._ensure_db_engine(connection_str=connection_str, connect_args=connect_args)
        engine = cls.__engines__[cls._get_dict_key(connection_str=connection_str, connect_args=connect_args)].engine
        return engine