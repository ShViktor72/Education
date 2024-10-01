# Добавление нескольких записей в таблицы
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from ORM_tables import Faculty, Student

# Настройка подключения
DATABASE_URL = 'mysql+pymysql://root:1234@localhost/python_db2'
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# 1. Добавление нескольких факультетов
faculties = [
    Faculty(name='Факультет математики'),
    Faculty(name='Факультет физики'),
    Faculty(name='Гуманитарный факультет')
]

session.add_all(faculties)  # Добавляем все факультеты в сессию
session.commit()  # Сохраняем изменения в базе данных

# 2. Получаем созданные факультеты для добавления студентов
it_faculty = session.query(Faculty).filter_by(name='Факультет информационных технологий').first()
math_faculty = session.query(Faculty).filter_by(name='Факультет математики').first()
physic_faculty = session.query(Faculty).filter_by(name='Факультет физики').first()
hum_faculty = session.query(Faculty).filter_by(name='Гуманитарный факультет').first()

# 3. Добавление нескольких студентов
students = [
    Student(name='Мария Петрова', faculty=it_faculty),
    Student(name='Сергей Сергеев', faculty=math_faculty),
    Student(name='Ольга Кузнецова', faculty=math_faculty),
    Student(name='Мария Егорова', faculty=physic_faculty),
    Student(name='Никита Сергеев', faculty=hum_faculty),
    Student(name='Ольга Федорова', faculty=hum_faculty),
]

session.add_all(students)  # Добавляем всех студентов в сессию
session.commit()  # Сохраняем изменения в базе данных

# Закрытие сессии
session.close()
