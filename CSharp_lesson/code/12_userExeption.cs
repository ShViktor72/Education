using System.IO;
namespace ConsoleApp
{
    public class InvalidAgeException : Exception
    {
        public InvalidAgeException(string message) : base(message)
        {
        }
    }

    internal class Program
    {
        public static void CheckAge(int age)
        {
            if (age < 0 || age > 100)
            {
                throw new InvalidAgeException("Возраст должен быть в диапазоне от 0 до 100");
            }
        }
        static void Main(string[] args)
        {
            // Пример использования:
            try
            {
                Console.WriteLine("Введите возраст: ");
                int enteredAge = int.Parse(Console.ReadLine());
                CheckAge(enteredAge);
                Console.WriteLine("Введенный возраст корректен.");
            }
            catch (InvalidAgeException ex)
            {
                Console.WriteLine("Ошибка: " + ex.Message);
            }
        }
    }
}






