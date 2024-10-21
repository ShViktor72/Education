using System;
using System.IO;

class Program
{
    static void Main()
    {
        string filePath = "example.txt";
        StreamReader reader = null;

        try
        {
            reader = new StreamReader(filePath);
            string content = reader.ReadToEnd();
            Console.WriteLine(content);
        }
        catch (FileNotFoundException ex)
        {
            Console.WriteLine("Файл не найден: " + ex.Message);
        }
        catch (IOException ex)
        {
            Console.WriteLine("Ошибка ввода-вывода: " + ex.Message);
        }
        catch (Exception ex)
        {
            Console.WriteLine("Произошло исключение: " + ex.Message);
        }
        finally
        {
            // Гарантированное закрытие файла, если он был открыт
            if (reader != null)
            {
                reader.Close();
            }
            Console.WriteLine("Закрытие файла.");
        }
    }
}
