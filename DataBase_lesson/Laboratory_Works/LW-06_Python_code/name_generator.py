# encoding_converter.py

import codecs

input_file = 'C:\\Users\\User\\Desktop\\College2024\\DataBase\\data\\pilevin.txt'  # Укажите путь к вашему файлу
output_file = 'C:\\Users\\User\\Desktop\\College2024\\DataBase\\data\\pilevin_utf8.txt'  # Путь для сохранения преобразованного файла

# Читаем файл с одной кодировкой и сохраняем в другой
with codecs.open(input_file, 'r', encoding='windows-1251') as f:
    content = f.read()

with codecs.open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Файл успешно преобразован.")
