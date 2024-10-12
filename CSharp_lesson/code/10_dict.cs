using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Создаем словарь для хранения данных о студентах
        Dictionary<int, string> students = new Dictionary<int, string>();

        // Добавляем элементы
        students.Add(1, "Alice");
        students.Add(2, "Bob");
        students.Add(3, "Charlie");

        // Получаем значение по ключу
        string studentName = students[2];
        Console.WriteLine($"Студент с ID 2: {studentName}");

        // Изменяем значение по ключу
        students[2] = "Robert";

        // Проверяем наличие ключа
        if (students.ContainsKey(3))
        {
            Console.WriteLine("Студент с ID 3 найден.");
        }

        // Удаляем элемент по ключу
        students.Remove(1);

        // Перебираем все элементы словаря
        foreach (var kvp in students)
        {
            Console.WriteLine($"ID: {kvp.Key}, Имя: {kvp.Value}");
        }
    }
}
