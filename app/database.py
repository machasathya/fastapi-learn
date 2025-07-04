from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

sql_database_url = "mysql+pymysql://root:Macha123@localhost:3306/demo_db"
engine = create_engine(sql_database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base()



# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:    
        db.close()  