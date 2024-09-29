using System;
using System.Collections.Generic;

class Program
{
    static string[] hangmanStages = new string[]
    {
        @"
        
        

        ",
        @"
         |
         |
         |
         |
         |
        ",
        @"
         ------
         |
         |
         |
         |
         |
        ",
        @"
         ------
         |    |
         |    
         |    
         |    
         |    
        ",
        @"
         ------
         |    |
         |    O
         |    
         |    
         |    
        ",
        @"
         ------
         |    |
         |    O
         |    |
         |    
         |    
        ",
        @"
         ------
         |    |
         |    O
         |   /|
         |    
         |    
        ",
        @"
         ------
         |    |
         |    O
         |   /|\
         |    
         |    
        ",
        @"
         ------
         |    |
         |    O
         |   /|\
         |   /
         |    
        ",
        @"
         ------
         |    |
         |    O
         |   /|\
         |   / \
         |    
        "
    };

    static string[] words = { "computer", "programmer", "hangman", "keyboard", "monitor" };
    static Random random = new Random();
    static string wordToGuess;
    static char[] guessedWord;
    static HashSet<char> guessedLetters;
    static int attemptsLeft;

    static void Main()
    {
        StartGame();
        while (attemptsLeft > 0 && new string(guessedWord) != wordToGuess)
        {
            Console.Clear();
            DisplayHangman();
            Console.WriteLine($"Слово: {new string(guessedWord)}");
            Console.Write("Введите букву: ");
            char guess = char.ToLower(Console.ReadKey().KeyChar);
            Console.WriteLine();

            if (guessedLetters.Contains(guess))
            {
                Console.WriteLine("Вы уже угадали эту букву.");
                continue;
            }

            guessedLetters.Add(guess);

            if (wordToGuess.Contains(guess))
            {
                for (int i = 0; i < wordToGuess.Length; i++)
                {
                    if (wordToGuess[i] == guess)
                    {
                        guessedWord[i] = guess;
                    }
                }
            }
            else
            {
                attemptsLeft--;
            }
        }

        Console.Clear();
        DisplayHangman();
        if (new string(guessedWord) == wordToGuess)
        {
            Console.WriteLine($"Поздравляем! Вы угадали слово: {wordToGuess}");
        }
        else
        {
            Console.WriteLine($"Вы проиграли. Загаданное слово было: {wordToGuess}");
        }
    }

    static void StartGame()
    {
        wordToGuess = words[random.Next(words.Length)];
        guessedWord = new string('_', wordToGuess.Length).ToCharArray();
        guessedLetters = new HashSet<char>();
        attemptsLeft = hangmanStages.Length - 1;
    }

    static void DisplayHangman()
    {
        Console.WriteLine(hangmanStages[hangmanStages.Length - attemptsLeft - 1]);
    }
}