using System;
internal class Program
{
    static void PrintNum(uint n)
    {
        uint numberUint = n;
        string binaryUint = Convert.ToString(numberUint, 2); // преобразует число numberInt в двоичную строку.
        Console.WriteLine($"число {n} в формате uint (4 байта) : {numberUint}");
        Console.WriteLine(binaryUint.PadLeft(32, '0')); // добавляем нули в старших разрядах до 32 символов
        Console.WriteLine();

        ushort numberUshort = (ushort)numberUint; // явное приведение (сужение) числа к типу ushort
        string binaryUshort = Convert.ToString(numberUshort, 2).PadLeft(16, '0'); // добавляем нули в старших разрядах до 16 символов
        Console.WriteLine($"число {n} приведенное к ushort (2 байта) : {numberUshort}");
        Console.WriteLine(binaryUshort.PadLeft(32)); // вравниваем строку по правому краю
        Console.WriteLine();

        byte numberByte = (byte)numberUshort; // / явное приведение (сужение) числа к типу byte
        string binaryByte = Convert.ToString(numberByte, 2).PadLeft(8, '0'); // добавляем нули в старших разрядах до 8 символов
        Console.WriteLine($"число {n} приведенное к byte (1 байт) : {numberByte}");
        Console.WriteLine(binaryByte.PadLeft(32)); // вравниваем строку по правому краю
        Console.WriteLine();
    }
    static void PrintNum2(int n)
    {
        int numberInt = n;
        string binaryInt = Convert.ToString(numberInt, 2); // преобразует число numberInt в двоичную строку.
        Console.WriteLine($"число {n} в формате int (4 байта) : {numberInt}");
        Console.WriteLine(binaryInt.PadLeft(32, '0')); // добавляем нули в старших разрядах до 32 символов
        Console.WriteLine();

        short numberShort = (short)numberInt; // явное приведение (сужение) числа к типу short
        string binaryShort = Convert.ToString(numberShort, 2).PadLeft(16, '0'); // добавляем нули в старших разрядах до 16 символов
        Console.WriteLine($"число {n} приведенное к short (2 байта) : {numberShort}");
        Console.WriteLine(binaryShort.PadLeft(32)); // вравниваем строку по правому краю
        Console.WriteLine();

        sbyte numberSbyte = (sbyte)numberShort; // / явное приведение (сужение) числа к типу sbyte
        string binarySbyte = Convert.ToString(numberSbyte, 2).PadLeft(8, '0'); // добавляем нули в старших разрядах до 8 символов
        Console.WriteLine($"число {n} приведенное к sbyte (1 байт) : {numberSbyte}");
        Console.WriteLine(binarySbyte.PadLeft(32)); // вравниваем строку по правому краю
    }
    static void Main(string[] args)
    {
        //PrintNum(10000);
        PrintNum2(-155);
    }
}