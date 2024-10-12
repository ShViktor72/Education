using System;
namespace MyApp
{
    internal class Program
    {
        // 1. Функция с параметрами. Невозращающая значение
        static void PrintSum(int a, int b)
        {
            int sum = a + b;
            Console.WriteLine("Сумма: " + sum);
        }

        // 2. Функция, возвращающая значение
        static int Square(int x)
        {
            return x * x;
        }

        // 3. Функция с несколькими параметрами и возвращаемым значением
        static int Max(int a, int b)
        {
            return (a > b) ? a : b;
        }

        // 4. Функция с использованием ключевого слова ref
        static void DoubleValue(ref int x)
        {
            x *= 2;
        }

        // 5. Функция с использованием ключевого слова out
        static void Calculate(int a, int b, out int sum, out int difference)
        {
            sum = a + b;
            difference = a - b;
        }

        // 6. Рекурсивная функция
        static int Factorial(int n)
        {
            if (n == 0)
                return 1;
            else
                return n * Factorial(n - 1);
        }

        // 7. Функция, принимающая массив в качестве параметра
        static int SumArray(int[] numbers)
        {
            int sum = 0;
            foreach (int number in numbers)
            {
                sum += number;
            }
            return sum;
        }

        static void Main(string[] args)
        {
            PrintSum(5, 10); // 1. Вызов функции с передачей аргументов

            int result = Square(4); // 2. Вызов функции и сохранение результата
            Console.WriteLine("Квадрат числа 4: " + result);

            int maxValue = Max(7, 10); // 3. Вызов функции
            Console.WriteLine("Максимальное значение: " + maxValue);

            int number = 5;
            DoubleValue(ref number); // 4. Передача параметра по ссылке
            Console.WriteLine("Удвоенное значение: " + number);

            int sum, difference;
            Calculate(10, 5, out sum, out difference); //5. Вызов функции с `out` параметрами
            Console.WriteLine("Сумма: " + sum);
            Console.WriteLine("Разность: " + difference);

            int res = Factorial(5); // 6. Вызов рекурсивной функции
            Console.WriteLine("Факториал 5: " + res);

            int[] myArray = { 1, 2, 3, 4, 5 };
            int sumArr = SumArray(myArray); // 7. Вызов функции
            Console.WriteLine("Сумма элементов массива: " + sumArr);
        }

    }
}