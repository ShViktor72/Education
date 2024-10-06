# Добавление  записей в таблицы
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from ORM_tables import Faculty, Student

# Настройка подключения
# DATABASE_URL = 'mysql+pymysql://username:password@localhost/db_name'
DATABASE_URL = 'mysql+pymysql://root:1234@localhost/python_db2'
engine = create_engine(DATABASE_URL)
Base = declarative_base()


# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# 3.1 Добавление данных
new_faculty = Faculty(name='Факультет информационных технологий')
session.add(new_faculty)
session.commit()

new_student = Student(name='Иван Иванов', faculty=new_faculty)
session.add(new_student)
session.commit()

# Закрытие сессии
session.close()
