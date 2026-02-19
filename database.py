from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)

def init_db():
    Base.metadata.create_all(bind=engine)


def seed_users():
    db = SessionLocal()
    try:
        if db.query(UserDB).count() == 0:
            users = [
                UserDB(name="blvdesgrxve", email="blvdesgrxve@gmail.com"),
                UserDB(name="tochka", email="tochka@gmail.com"),
                UserDB(name="sdf", email="sdf@gmail.com"),
                UserDB(name="trm", email="trm@gmail.com"),
                UserDB(name="rtk", email="rtk@gmail.com"),
            ]
            db.add_all(users)
            db.commit()
            print(f"Добавлено {len(users)} пользователей")
    except Exception as e:
        db.rollback()
        print(f"Ошибка инициализации: {e}")
    finally:
        db.close()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()