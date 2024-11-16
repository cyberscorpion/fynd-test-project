from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

DATABASE_URL = "sqlite:///database.db"

engine = create_engine('mysql+pymysql://pirayanshjain:fyndtest123@pirayanshjain.mysql.pythonanywhere-services.com:3306/fynd')
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()