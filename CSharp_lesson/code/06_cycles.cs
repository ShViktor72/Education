// цикл for
// Вывод чисел от 1 до 10
Console.WriteLine("Вывод чисел от 1 до 10");
for (int i = 1; i <= 10; i++)
{
	Console.WriteLine(i);
}

// Вывод чётных чисел от 2 до 20
Console.WriteLine("Вывод чётных чисел от 2 до 20");
for (int i = 2; i <= 20; i += 2)
{
	Console.WriteLine(i);
}

// Обратный отсчёт от 10 до 1
Console.WriteLine("Обратный отсчёт от 10 до 1");
for (int i = 10; i >= 1; i--)
{
	Console.WriteLine(i);
}

// Перебор элементов массива
Console.WriteLine("Перебор элементов массива");
string[] fruits = { "Яблоко", "Банан", "Вишня", "Манго", "Груша" };

for (int i = 0; i < fruits.Length; i++)
{
	Console.WriteLine(fruits[i]);
}

// цикл while..do
// Вывод чисел от 1 до 5
Console.WriteLine("while. Вывод чисел от 1 до 5");
int j = 1;

while (j <= 5)
{
	Console.WriteLine(j);
	j++;
}

// Подсчёт суммы чисел от 1 до 100
Console.WriteLine("Подсчёт суммы чисел от 1 до 100");
j = 1;
int sum = 0;

while (j <= 100)
{
	sum += j;
	j++;
}

Console.WriteLine("Сумма чисел от 1 до 100: " + sum);

// Поиск первого чётного числа в массиве
Console.WriteLine("Поиск первого чётного числа в массиве");
int[] numbers = { 3, 7, 5, 9, 4, 2 };
j = 0;

while (j < numbers.Length)
{
	if (numbers[j] % 2 == 0)
	{
		Console.WriteLine("Первое четное число: " + numbers[j]);
		break;
	}
	j++;
}

// Ввод чисел до тех пор, пока не введено отрицательное число
Console.WriteLine("Ввод чисел до тех пор, пока не введено отрицательное число");
int number;
while (true)
{
	Console.Write("Введите число: ");
	number = int.Parse(Console.ReadLine());

	if (number < 0)
	{
		Console.WriteLine("Введено отрицательное число. Цикл завершен.");
		break;
	}
}

// цикл do..while
// Вывод чисел от 1 до 5
Console.WriteLine("Вывод чисел от 1 до 5");
j = 1;

do
{
	Console.WriteLine(j);
	j++;
} while (j <= 5);


// Запрос ввода пользователя до тех пор, пока не будет введено число больше 0
Console.WriteLine("Запрос ввода пользователя до тех пор, пока не будет введено число больше 0");
int num;

do
{
	Console.Write("Введите положительное число: ");
	num = int.Parse(Console.ReadLine());
} while (num <= 0);

Console.WriteLine("Вы ввели: " + num);