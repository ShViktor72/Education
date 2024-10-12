// Свойства класса String
// Length: Возвращает длину строки(количество символов).
string example = "Hello, World!";
int length = example.Length;
Console.WriteLine(length); // Выведет 13

// Chars[int index]: Позволяет получить символ в строке по указанному индексу (аналогично example[index])
char firstChar = example[0];
Console.WriteLine(firstChar); // Выведет 'H'

// Основные методы класса String. Substring(int startIndex, int length)
// Извлекает подстроку, начиная с указанного индекса и заданной длины.
string text = "Hello, World!";
string sub = text.Substring(7, 5);
Console.WriteLine(sub); // Выведет "World"

// IndexOf(string value)
// Возвращает индекс первого вхождения подстроки в строку.
int index = text.IndexOf("World");
Console.WriteLine(index); // Выведет 7

// ToUpper() и ToLower()
// Преобразует строку в верхний или нижний регистр.
string upper = text.ToUpper();
string lower = text.ToLower();

Console.WriteLine(upper); // Выведет "HELLO, WORLD!"
Console.WriteLine(lower); // Выведет "hello, world!"

// Replace(string oldValue, string newValue)
// Заменяет все вхождения указанной подстроки на другую подстроку.
string replaced = text.Replace("World", "C#");

Console.WriteLine(replaced); // Выведет "Hello, C#!"

// Split(char[] separator)
// Разбивает строку на массив подстрок, используя указанные символы - разделители.
text = "apple,banana,cherry";
string[] fruits = text.Split(',');

foreach (string fruit in fruits)
{
	Console.WriteLine(fruit); // Выведет "apple", "banana", "cherry"
}

// Trim(), TrimStart(), TrimEnd()
// Удаляют пробелы или указанные символы из начала и/ или конца строки.
text = "   Hello, World!   ";
string trimmed = text.Trim();
string trimmedStart = text.TrimStart();
string trimmedEnd = text.TrimEnd();

Console.WriteLine(trimmed);       // Выведет "Hello, World!"
Console.WriteLine(trimmedStart);  // Выведет "Hello, World!   "
Console.WriteLine(trimmedEnd);    // Выведет "   Hello, World!"

// Contains(string value)
// Возвращает true, если строка содержит указанную подстроку.
text = "Hello, World!";
bool contains = text.Contains("World");

Console.WriteLine(contains); // Выведет "True"

// StartsWith(string value) и EndsWith(string value)
// Проверяют, начинается ли или заканчивается строка указанной подстрокой.
text = "Hello, World!";
bool startsWith = text.StartsWith("Hello");
bool endsWith = text.EndsWith("World!");

Console.WriteLine(startsWith); // Выведет "True"
Console.WriteLine(endsWith);   // Выведет "True"

// StartsWith(string value) и EndsWith(string value)
// Проверяют, начинается ли или заканчивается строка указанной подстрокой.
startsWith = text.StartsWith("Hello");
endsWith = text.EndsWith("World!");

Console.WriteLine(startsWith); // Выведет "True"
Console.WriteLine(endsWith);   // Выведет "True"

// Join(string separator, string[] value)
// Объединяет элементы массива строк в одну строку, используя указанный разделитель.
string[] words = { "apple", "banana", "cherry" };
string joined = string.Join(", ", words);

Console.WriteLine(joined); // Выведет "apple, banana, cherry"

// Compare(string strA, string strB)
// Сравнивает две строки и возвращает целое число, которое указывает их относительное положение в сортировке.
int comparison = string.Compare("apple", "banana");

if (comparison < 0)
	Console.WriteLine("apple идет перед banana");
else if (comparison > 0)
	Console.WriteLine("apple идет после banana");
else
	Console.WriteLine("apple и banana равны");

// Изменение регистра, поиск и замена
text = "The quick brown fox jumps over the lazy dog.";
text = text.ToLower();
text = text.Replace("quick", "slow");
int position = text.IndexOf("fox");

Console.WriteLine(text); // Выведет "the slow brown fox jumps over the lazy dog."
Console.WriteLine("Position of 'fox': " + position); // Выведет "Position of 'fox': 14"

// Разделение и сборка строки
text = "one,two,three,four";
string[] parts = text.Split(',');

foreach (string part in parts)
{
	Console.WriteLine(part);
}

string rejoined = string.Join(" - ", parts);
Console.WriteLine(rejoined); // Выведет "one - two - three - four" 