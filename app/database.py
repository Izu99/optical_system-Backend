from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Replace with your actual database URL
DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/optical_system"

# Create an SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define the sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for declarative models
Base = declarative_base()

def test_connection():
    try:
        # Try to connect to the database
        with engine.connect() as connection:
            print("Database connection successful!")
    except OperationalError as e:
        print(f"Database connection failed: {e}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    test_connection()
