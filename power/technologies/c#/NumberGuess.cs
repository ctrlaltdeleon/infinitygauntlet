using System;

class Driver
{
    static void Main(string[] args)
    {
        GetAppInfo();
        GreetUser();

        while (true)
        {

            // Create a random object that then assigns a random number to `correctNumber`.
            Random random = new Random();
            int correctNumber = random.Next(1, 11);

            int guess = 0;

            while (guess != correctNumber)
            {
                Console.WriteLine("Guess a number between 1 and 10:");
                string input = Console.ReadLine();

                // Check if it's an integer.
                if (!int.TryParse(input, out guess))
                {
                    Message(ConsoleColor.Red, "Please enter a valid number!");
                    // Passes control to the next iteration of either while, do, for, or foreach.
                    continue;
                }

                guess = Int32.Parse(input);

                if (guess < correctNumber)
                {
                    Console.WriteLine("Go higher!");
                }
                else if (guess > correctNumber)
                {
                    Console.WriteLine("Go lower!");
                }
            }

            Message(ConsoleColor.Green, "Congrats you won!");

            Console.WriteLine("Play Again? [Y or N]");

            string answer = Console.ReadLine().ToUpper();

            if (answer == "Y")
            {
                continue;
            }
            else if (answer == "N")
            {
                return;
            }
            else
            {
                // Quits otherwise no matter the answer.
                return;
            }
        }
    }

    static void GetAppInfo()
    {
        string appName = "Number Guesser";
        string appVersion = "1.0.0";
        string appAuthor = "AC De Leon";

        // Change text color.
        Console.ForegroundColor = ConsoleColor.Yellow;

        Console.WriteLine($"{appName}: Version {appVersion} by {appAuthor}");

        Console.ResetColor();
    }

    static void GreetUser()
    {
        Console.Write("What is your name? ");

        string username = Console.ReadLine();

        Console.WriteLine($"Hello {username}, let's play a game!");
    }

    static void Message(ConsoleColor color, string message)
    {
        Console.ForegroundColor = color;

        Console.WriteLine(message);

        Console.ResetColor();
    }
}