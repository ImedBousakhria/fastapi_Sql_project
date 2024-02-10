from sqlalchemy import create_engine
from slqalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./myDB.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_tread": False } )
SessionLocal= sessionmaker(aut)