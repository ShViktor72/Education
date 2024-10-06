# выборка и обновление (select, update)
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

# Запрос на выборку данных
# students = session.query(Student).all()
# for student in students:
#     print(f'Студент: {student.name}, Факультет: {student.faculty.name}')

# Обновление данных
# student_to_update = session.query(Student).filter_by(name='Ольга Кузнецова').first()
# if student_to_update:
#     student_to_update.name = 'Ольга Степанова'
#     session.commit()

# Проверим, что данные обновились
print('Проверим, что данные обновились')
student_name = 'Ольга Степанова'
student = session.query(Student).filter(Student.name == student_name).first()
if student:
    print(f'Студент: {student.name}, Факультет: {student.faculty.name}')
else:
    print('Студент не найден.')


# Закрытие сессии
session.close()
