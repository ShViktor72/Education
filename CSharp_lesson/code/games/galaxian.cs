using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

class Program
{
    static int screenWidth = 40;
    static int screenHeight = 20;
    static char playerChar = '^';
    static char enemyChar = 'V';
    static char bulletChar = '|';
    static int playerX;
    static int playerY;
    static List<(int X, int Y)> enemies = new List<(int X, int Y)>();
    static List<(int X, int Y)> bullets = new List<(int X, int Y)>();
    static Random random = new Random();
    static bool gameOver = false;
    static int enemyMoveInterval = 2000; // Интервал обновления движения врагов в миллисекундах
    static int enemyMoveTimer = 0;

    static void Main()
    {
        Console.CursorVisible = false;
        Console.SetWindowSize(screenWidth, screenHeight);
        Console.SetBufferSize(screenWidth, screenHeight);

        playerX = screenWidth / 2;
        playerY = screenHeight - 2;

        InitializeEnemies();

        Task.Run(() => GameLoop());

        while (!gameOver)
        {
            HandleInput();
        }

        Console.Clear();
        Console.SetCursorPosition(screenWidth / 2 - 6, screenHeight / 2);
        Console.WriteLine("Game Over!");
    }

    static void InitializeEnemies()
    {
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                enemies.Add((5 + j * 2, 2 + i));
            }
        }
    }

    static void GameLoop()
    {
        DateTime lastEnemyMove = DateTime.Now;

        while (!gameOver)
        {
            DateTime now = DateTime.Now;
            TimeSpan elapsedTime = now - lastEnemyMove;

            if (elapsedTime.TotalMilliseconds >= enemyMoveInterval)
            {
                UpdateEnemies();
                lastEnemyMove = now;
            }

            UpdateBullets();
            CheckCollisions();
            Render();
            Thread.Sleep(100); // Пауза для плавности обновления экрана
        }
    }

    static void HandleInput()
    {
        if (Console.KeyAvailable)
        {
            ConsoleKey key = Console.ReadKey(true).Key;

            switch (key)
            {
                case ConsoleKey.LeftArrow:
                    if (playerX > 1) playerX--;
                    break;
                case ConsoleKey.RightArrow:
                    if (playerX < screenWidth - 2) playerX++;
                    break;
                case ConsoleKey.Spacebar:
                    bullets.Add((playerX, playerY - 1));
                    break;
            }
        }
    }

    static void UpdateBullets()
    {
        var newBullets = new List<(int X, int Y)>();

        foreach (var bullet in bullets)
        {
            if (bullet.Y > 0)
            {
                newBullets.Add((bullet.X, bullet.Y - 1));
            }
        }

        bullets = newBullets;
    }

    static void UpdateEnemies()
    {
        for (int i = 0; i < enemies.Count; i++)
        {
            var enemy = enemies[i];
            enemies[i] = (enemy.X, enemy.Y + 1);

            if (enemy.Y >= screenHeight - 1)
            {
                gameOver = true;
            }
        }

        // Randomly move enemies horizontally
        foreach (var i in Enumerable.Range(0, enemies.Count))
        {
            if (random.Next(2) == 0)
            {
                var (x, y) = enemies[i];
                enemies[i] = (x + (random.Next(2) == 0 ? 1 : -1), y);
            }
        }
    }

    static void CheckCollisions()
    {
        var hitEnemies = new HashSet<(int X, int Y)>();
        var hitBullets = new HashSet<(int X, int Y)>();

        foreach (var bullet in bullets)
        {
            foreach (var enemy in enemies)
            {
                if (bullet.X == enemy.X && bullet.Y == enemy.Y)
                {
                    hitEnemies.Add(enemy);
                    hitBullets.Add(bullet);
                    break;
                }
            }
        }

        enemies = enemies.Except(hitEnemies).ToList();
        bullets = bullets.Except(hitBullets).ToList();

        if (enemies.Count == 0)
        {
            Console.Clear();
            Console.SetCursorPosition(screenWidth / 2 - 8, screenHeight / 2);
            Console.WriteLine("You Win!");
            gameOver = true;
        }
    }

    static void Render()
    {
        Console.Clear();

        // Draw player
        Console.SetCursorPosition(playerX, playerY);
        Console.Write(playerChar);

        // Draw enemies
        foreach (var enemy in enemies)
        {
            Console.SetCursorPosition(enemy.X, enemy.Y);
            Console.Write(enemyChar);
        }

        // Draw bullets
        foreach (var bullet in bullets)
        {
            Console.SetCursorPosition(bullet.X, bullet.Y);
            Console.Write(bulletChar);
        }
    }
}
