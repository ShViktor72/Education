# удаление записи (delete)
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

student_name = 'Иван Иванов'
student = session.query(Student).filter(Student.name == student_name).first()

if student:
    session.delete(student)
    session.commit()
    print(f'Студент {student.name} успешно удален.')
else:
    print('Студент не найден.')
# Закрытие сессии
session.close()