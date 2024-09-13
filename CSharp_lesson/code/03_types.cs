// типы данных
// символ
char a = 'A';  // одинарные кавычки
			   // строка
string hello = "Hello"; // двойные кавычки

//  целые числа без знака
byte numByte = 255;                           // 1 байт
ushort numUshort = 65535;                     // 2 байта
uint numUint = 4_294_967_295;                 // 4 байта
ulong numUlong = 18_446_744_073_709_551_615;  // 8 байт

// целые числа со знаком
sbyte mumSbyte = -127;                        // 1 байт 
short numShort = -32767;                      // 2 байта
int numInt = -2_147_483_648;                  // 4 байта
long numLong = -922337203;                    // 8 байт

// Числа с плавающей точкой
float numFloat = 3.14f;      // 4 байта, указывается литерал F
double numDouble = 123.456;  // 8 байт, тип по умолчанию
decimal numDecimal = 1000.98765M; // 16 байт, литерал M

// неявное приведение типов
numInt = 100;
numLong = numByte;

numFloat = 7.62f;
numDouble = numFloat;

Console.WriteLine("неявное приведение типов");
Console.WriteLine($"numLog = {numLong}");
Console.WriteLine($"numFloat = {numFloat}");


// явное приведение типов без потерь
Console.WriteLine();
Console.WriteLine("явное приведение типов без потерь");

numLong = 1000;
numInt = (int)numLong; // 1000
Console.WriteLine($"numInt = {numInt}");

numDouble = 10.25;
numFloat = (float)numDouble; // 10.25
Console.WriteLine($"numFloat = {numFloat}");

numFloat = 100.0f;
numInt = (int) numFloat; // 10     
Console.WriteLine($"numInt = {numInt}");



// явное приведение типов c потерями
Console.WriteLine();
Console.WriteLine("явное приведение типов c потерями");
numDouble = 123.456;
numInt = (int)numDouble;  // 123, дробная часть потеряна
Console.WriteLine($"numInt = {numInt}");

numInt = 1000; // Это значение больше максимального значения byte
numByte = (byte) numInt;
Console.WriteLine($"numByte = {numByte}");

numShort = -123; // число со знаком
numUshort = (ushort) numShort; // ushort не может быть отрицательным
Console.WriteLine($"numUshort = {numUshort}");