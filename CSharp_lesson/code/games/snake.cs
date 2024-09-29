using System;
using System.Collections.Generic;
using System.Threading;

class Program
{
    static void Main()
    {
        int width = 40;
        int height = 20;
        int score = 0;
        bool gameOver = false;
        Console.CursorVisible = false;

        // Позиция змейки и еды
        List<int[]> snake = new List<int[]>();
        snake.Add(new int[] { width / 2, height / 2 });

        int[] food = new int[] { new Random().Next(1, width - 1), new Random().Next(1, height - 1) };
        int[] direction = new int[] { 0, 1 }; // Начальное направление (вправо)

        while (!gameOver)
        {
            Console.Clear();

            // Рисуем границы
            for (int i = 0; i < width; i++) Console.Write("-");
            Console.WriteLine();
            for (int i = 0; i < height; i++) Console.WriteLine("|" + new string(' ', width - 2) + "|");
            for (int i = 0; i < width; i++) Console.Write("-");

            // Рисуем еду
            Console.SetCursorPosition(food[0], food[1]);
            Console.Write("O");

            // Двигаем змейку
            int[] newHead = new int[] { snake[0][0] + direction[0], snake[0][1] + direction[1] };
            snake.Insert(0, newHead);

            // Проверка на столкновение со стенами
            if (newHead[0] == 0 || newHead[0] == width - 1 || newHead[1] == 0 || newHead[1] == height - 1)
            {
                gameOver = true;
            }

            // Проверка на столкновение с хвостом
            for (int i = 1; i < snake.Count; i++)
            {
                if (snake[i][0] == newHead[0] && snake[i][1] == newHead[1])
                {
                    gameOver = true;
                }
            }

            // Проверка на поедание еды
            if (newHead[0] == food[0] && newHead[1] == food[1])
            {
                score++;
                food = new int[] { new Random().Next(1, width - 1), new Random().Next(1, height - 1) };
            }
            else
            {
                snake.RemoveAt(snake.Count - 1);
            }

            // Рисуем змейку
            foreach (int[] segment in snake)
            {
                Console.SetCursorPosition(segment[0], segment[1]);
                Console.Write("*");
            }

            // Управление змейкой
            if (Console.KeyAvailable)
            {
                ConsoleKey key = Console.ReadKey(true).Key;
                switch (key)
                {
                    case ConsoleKey.W:
                        if (direction[1] != 1) direction = new int[] { 0, -1 };
                        break;
                    case ConsoleKey.S:
                        if (direction[1] != -1) direction = new int[] { 0, 1 };
                        break;
                    case ConsoleKey.A:
                        if (direction[0] != 1) direction = new int[] { -1, 0 };
                        break;
                    case ConsoleKey.D:
                        if (direction[0] != -1) direction = new int[] { 1, 0 };
                        break;
                }
            }

            Thread.Sleep(100);
        }

        Console.SetCursorPosition(width / 2 - 5, height / 2);
        Console.WriteLine("Игра окончена!");
        Console.SetCursorPosition(width / 2 - 7, height / 2 + 1);
        Console.WriteLine($"Ваш счет: {score}");
    }
}