using System;

class Driver
{
    static void Main(string[] args)
    {
        GuessingGame();

        Console.ReadLine();
    }

    static void GuessingGame()
    {
        Console.WriteLine("Guessing game! You have 3 tries to guess the secret word!");
        string secretWord = "yeet";
        string guess = "";
        int guessCount = 0;
        int guessLimit = 3;
        bool outOfGuesses = false;
        while (guess != secretWord && !outOfGuesses)
        {
            if (guessCount < guessLimit)
            {
                Console.Write("Enter a guess! ");
                guess = Console.ReadLine();
                guessCount++;
            }
            else
            {
                outOfGuesses = true;
            }
        }
        if (outOfGuesses)
        {
            Console.WriteLine("You lose!");
        }
        else
        {
            Console.WriteLine("You win!");
        }
    }
}