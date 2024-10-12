using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Создаем множества
        HashSet<int> set1 = new HashSet<int> { 1, 2, 3, 4, 5 };
        HashSet<int> set2 = new HashSet<int> { 4, 5, 6, 7, 8 };

        // Объединение множеств
        set1.UnionWith(set2);
        Console.WriteLine("Объединение: " + string.Join(", ", set1));

        // Пересечение множеств
        set1.IntersectWith(set2);
        Console.WriteLine("Пересечение: " + string.Join(", ", set1));

        // Разность множеств
        set1.ExceptWith(set2);
        Console.WriteLine("Разность: " + string.Join(", ", set1));

        // Симметрическая разность
        set1.SymmetricExceptWith(set2);
        Console.WriteLine("Симметрическая разность: " + string.Join(", ", set1));
    }
}
