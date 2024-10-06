# sqlalchemy Создание таблиц в базе данных
# pip install sqlalchemy pymysql
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base


# Настройка подключения
# DATABASE_URL = 'mysql+pymysql://username:password@localhost/db_name'
DATABASE_URL = 'mysql+pymysql://root:1234@localhost/python_db2'
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Определение модели Faculty
class Faculty(Base):
    __tablename__ = 'faculties'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    students = relationship('Student', back_populates='faculty')

# Определение модели Student
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    faculty_id = Column(Integer, ForeignKey('faculties.id'), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    faculty = relationship('Faculty', back_populates='students')

# Создание таблиц в базе данных
Base.metadata.create_all(engine)



