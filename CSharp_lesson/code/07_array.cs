// Одномерные массивы
// Создание и инициализация массива
int[] numbers = new int[5]; // Создание массива из 5 элементов

// Инициализация массива
numbers[0] = 10;
numbers[1] = 20;
numbers[2] = 30;
numbers[3] = 40;
numbers[4] = 50;

Console.WriteLine("Первый элемент: " + numbers[0]); // Вывод первого элемента
Console.WriteLine("Последний элемент: " + numbers[numbers.Length - 1]); // Вывод последнего элемента


// foreach
int[] numbers2 = { 10, 20, 30, 40, 50 }; // массив инициализируется значениями при создании

for (int i = 0; i < numbers2.Length; i++)
{
	Console.WriteLine("Элемент " + i + ": " + numbers2[i]);
}

// Использование цикла foreach для перебора элементов массива
string[] fruits = { "Яблоко", "Банан", "Вишня", "Груша", "Манго" }; // создается массив строк fruits

foreach (string fruit in fruits)
{
	Console.WriteLine(fruit);
}

// Нахождение максимального элемента в массиве
int[] nums = { 7, 2, 10, 4, 9 };
int max = nums[0];

foreach (int number in nums)
{
	if (number > max)
	{
		max = number;
	}
}

Console.WriteLine("Максимальный элемент: " + max);

// Подсчёт суммы элементов массива
int[] numbers3 = { 1, 2, 3, 4, 5 };
int sum = 0;

foreach (int number in numbers3)
{
	sum += number;
}

Console.WriteLine("Сумма элементов массива: " + sum);

// Многомерные массивы
// Создание и инициализация двумерного массива
int[,] matrix = new int[3, 3]; // Создание 3x3 двумерного массива

// Инициализация массива
matrix[0, 0] = 1;
matrix[0, 1] = 2;
matrix[0, 2] = 3;
matrix[1, 0] = 4;
matrix[1, 1] = 5;
matrix[1, 2] = 6;
matrix[2, 0] = 7;
matrix[2, 1] = 8;
matrix[2, 2] = 9;

Console.WriteLine("Элемент в позиции [1,1]: " + matrix[1, 1]); // Вывод элемента

// Перебор элементов двумерного массива с помощью вложенных циклов for
int[,] matrix2 =
{
{ 1, 2, 3 },
{ 4, 5, 6 },
{ 7, 8, 9 }
};

for (int i = 0; i < matrix2.GetLength(0); i++) // Перебор строк
{
	for (int j = 0; j < matrix2.GetLength(1); j++) // Перебор столбцов
	{
		Console.Write(matrix2[i, j] + " ");
	}
	Console.WriteLine(); // Переход на новую строку
}

// Перебор элементов двумерного массива с использованием цикла foreach
foreach (int element in matrix2)
{
	Console.Write(element + " ");
}

// Вычисление суммы всех элементов в двумерном массиве
int summ = 0;

foreach (int element in matrix)
{
	summ += element;
}

Console.WriteLine("Сумма всех элементов: " + summ);