using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Создаем список целых чисел
        List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };

        // Добавляем элементы
        numbers.Add(6);
        numbers.AddRange(new int[] { 7, 8, 9 });

        // Выводим список
        Console.WriteLine("Список чисел:");
        foreach (int number in numbers)
        {
            Console.WriteLine(number);
        }

        // Проверяем наличие элемента
        if (numbers.Contains(5))
        {
            Console.WriteLine("Число 5 есть в списке.");
        }

        // Удаляем элемент
        numbers.Remove(3);

        // Выводим обновленный список
        Console.WriteLine("Обновленный список:");
        foreach (int number in numbers)
        {
            Console.WriteLine(number);
        }

        // Сортируем список
        numbers.Sort();
        Console.WriteLine("Отсортированный список:");
        foreach (int number in numbers)
        {
            Console.WriteLine(number);
        }
    }
}

