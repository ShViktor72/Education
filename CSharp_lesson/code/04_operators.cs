// оператор присваивания
int n = 10;  // Оператор присваивания присваивает значение 10 переменной n
double m = 4.5;      // Присваиваем переменной m значение 4.5
string name = "John"; // Присваиваем переменной name значение "John"
bool isActive = true; // Присваиваем переменной isActive значение true

// Комбинированные операторы присваивания:
int x = 1;
x += 5;  // Эквивалентно x = x + 5; Теперь x равно 15
x -= 3;  // Эквивалентно x = x - 3; Теперь x равно 12
x *= 2;  // Эквивалентно x = x * 2; Теперь x равно 24
x /= 4;  // Эквивалентно x = x / 4; Теперь x равно 6
x %= 5;  // Эквивалентно x = x % 5; Теперь x равно 1

// Арифметические операторы.
int a = 20;
int b = 8;

// Сложение
int sum = a + b;  // sum = 28

// Вычитание
int difference = a - b;  // difference = 12

// Умножение
int product = a * b;  // product = 160

// Деление
int quotient = a / b;  // quotient = 2 (целочисленное деление)
double quotientDouble = (double)a / b;  // quotientDouble = 2.5 (деление с плавающей точкой)

// Остаток от деления
int remainder = a % b;  // remainder = 4


// Пример использования с числами с плавающей точкой
double z = 5.5;
double y = 2.0;

double add = z + y;   //  7.5
double diff = z - y;  //  3.5
double mult = z * y;  //  11.0
double div = z / y;   //  2.75

// Инкремент (++) и декремент (--)
int count = 10;
count++;  // count = 11

count = 10;
count--;  // count = 9



// Класс Math
//Math.Abs: Возвращает абсолютное значение числа.
int absValue = Math.Abs(-10);  // absValue = 10

//Math.Pow: Возвращает число, возведенное в указанную степень.
double power = Math.Pow(2, 3);  // power = 8.0 (2^3)

//Math.Sqrt: Возвращает квадратный корень числа.
double squareRoot = Math.Sqrt(16);  // squareRoot = 4.0

//Math.Round: Округляет число до ближайшего целого или указанного количества знаков после запятой.
double roundedValue = Math.Round(3.14159);  // roundedValue = 3
double roundedValue2 = Math.Round(3.14159, 2);  // roundedValue2 = 3.14

//Math.Max: Возвращает большее из двух чисел.
int max = Math.Max(10, 20);  // max = 20

//Math.Min: Возвращает меньшее из двух чисел.
int min = Math.Min(10, 20);  // min = 10

//Math.Ceiling: Возвращает наименьшее целое число, большее или равное указанному числу.
double ceilingValue = Math.Ceiling(4.2);  // ceilingValue = 5.0

//Math.Floor: Возвращает наибольшее целое число, меньшее или равное указанному числу.
double floorValue = Math.Floor(4.8);  // floorValue = 4.0

//Math.Sin, Math.Cos, Math.Tan: Возвращают синус, косинус и тангенс угла соответственно(в радианах).
double sinValue = Math.Sin(Math.PI / 2);  // sinValue = 1.0
double cosValue = Math.Cos(0);  // cosValue = 1.0
double tanValue = Math.Tan(Math.PI / 4);  // tanValue = 1.0

//Math.Asin, Math.Acos, Math.Atan: Возвращают арксинус, арккосинус и арктангенс соответственно(в радианах).
double asinValue = Math.Asin(1);  // asinValue = Math.PI / 2
double acosValue = Math.Acos(1);  // acosValue = 0
double atanValue = Math.Atan(1);  // atanValue = Math.PI / 4


//Math.Log: Возвращает логарифм числа по указанному основанию.
double logValue = Math.Log(8, 2);  // logValue = 3 (логарифм 8 по основанию 2)
double naturalLog = Math.Log(2.718281828);  // naturalLog = 1.0 (натуральный логарифм)


//Math.Exp: Возвращает e, возведенное в указанную степень.
double expValue = Math.Exp(1);  // expValue = 2.718281828 (e^1)

//Math.Sign: Возвращает знак числа(-1 для отрицательных чисел, 0 для нуля и 1 для положительных чисел).
int signValue = Math.Sign(-10);  // signValue = -1

//Основные свойства класса Math
//Math.PI: Константа, представляющая значение числа π(пи).
double piValue = Math.PI;  // piValue = 3.141592653589793

//Math.E: Константа, представляющая значение числа e(основание натуральных логарифмов).
double eValue = Math.E;  // eValue = 2.718281828459045

//Примеры использования класса Math
//Расчет длины окружности:
double radius = 5.0;
double circumference = 2 * Math.PI * radius;  // Длина окружности = 2πr

//Нахождение гипотенузы треугольника по теореме Пифагора:
double sideA = 3.0;
double sideB = 4.0;
double sideC = Math.Sqrt(Math.Pow(sideA, 2) + Math.Pow(sideB, 2));  // sideC = 5.0

//Округление числа до ближайшего целого:
double number = 4.567;
double roundedNumber = Math.Round(number);  // roundedNumber = 5

// Класс Console
//Console.WriteLine: Выводит строку текста на консоль с переходом на новую строку.
Console.WriteLine("Hello, World!");

//Console.Write: Выводит строку текста на консоль без перехода на новую строку.
Console.Write("Enter your name: ");

//Console.ReadLine: Считывает ввод пользователя до нажатия клавиши Enter и возвращает его в виде строки.
string Name = Console.ReadLine();

//Console.ReadKey: Считывает следующий ввод символа от пользователя. Можно настроить метод так, чтобы символ не отображался на экране.
Console.WriteLine("Press any key to continue...");
Console.ReadKey();  // Ожидает нажатия клавиши

//Console.Clear: Очищает консольное окно.
Console.Clear();  // Очистка экрана

//Console.Beep: Издает звуковой сигнал через динамик.
Console.Beep();  // Издает звук

//Console.ForegroundColor и Console.BackgroundColor: Устанавливают цвет текста и фона консоли.
Console.ForegroundColor = ConsoleColor.Red;
Console.BackgroundColor = ConsoleColor.Yellow;
Console.WriteLine("Red text on yellow background");
Console.ResetColor();  // Сбрасывает цвета к стандартным

// класс Convert
Console.WriteLine("Введите число: ");  // "123"
int intValue = Convert.ToInt32(Console.ReadLine());  // intValue = 123
Console.WriteLine("Введите число: ");  // "10.5"
float floatValue = Convert.ToSingle(Console.ReadLine());  // floatValue = 10.5F

// класс Random
Random rnd = new Random();
int randomNumber = rnd.Next();            // Случайное число от 0 до int.MaxValue
int randomNumber2 = rnd.Next(100);        // Случайное число от 0 до 99
int randomNumber3 = rnd.Next(50, 100);    // Случайное число от 50 до 99
double randomDouble = rnd.NextDouble();   // Случайное число от 0.0 до 1.0
/*Для воспроизводимости результатов можно задать начальное значение (сид) для генератора случайных чисел, 
передав его в конструктор Random. Это гарантирует, что последовательность случайных чисел будет одинаковой 
при каждом запуске программы.*/
Random rand = new Random(42);  // Использование сида 42 для генератора
int randomNumber4 = rand.Next(1, 101);  // Последовательность чисел будет повторяться при каждом запуске

Console.WriteLine(randomNumber4);



