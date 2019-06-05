using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// 3:15:25 / 4:31:08

namespace Giraffe
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Strings!");
            string phrase = "nice one";
            Console.WriteLine(phrase[0]); // "n".
            Console.WriteLine(phrase.IndexOf("one")); // Finds the first occurrence, which is at 5.

            Console.WriteLine("Numbers!");
            int num = 5;
            Console.WriteLine(num / 2); // Returns an integer.
            Console.WriteLine(num / 2.0); // Returns a decimal.
            Console.WriteLine(Math.Abs(-num)); // Calling methods.
            Console.WriteLine(Math.Max(num, num + 5)); // Finds the max number between 2 parameters.

            Console.WriteLine("User input!");
            Console.WriteLine("Enter your name: ");
            string name = Console.ReadLine(); // Allocate user input to a string data type.
            Console.WriteLine("Hello " + name);

            Console.WriteLine("Addition calculator!");
            Console.WriteLine("Enter a number: ");
            double num1 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter another number: ");
            double num2 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(num1 + num2);

            Console.WriteLine("Mad lib!");
            string color, pluralNoun, celebrity;
            Console.WriteLine("Enter a color: ");
            color = Console.ReadLine();
            Console.WriteLine("Enter a plural noun: ");
            pluralNoun = Console.ReadLine();
            Console.WriteLine("Enter a celebrity: ");
            celebrity = Console.ReadLine();
            Console.WriteLine("Roses are " + color);
            Console.WriteLine(pluralNoun + " are blue");
            Console.WriteLine("I love " + celebrity);

            Console.WriteLine("Arrays!");
            int[] luckyNumbers = { 4, 8, 15, 42, 69, 420 };
            string[] friends = new string[5]; // Creating an empty allocation for an array of strings.
            Console.WriteLine(luckyNumbers[5]);

            Console.WriteLine("Methods!");
            SayHi("AC");
            SayHi("Sora");
            SayHi("Mega Man");
            Console.WriteLine(Cubed(3));

            Console.WriteLine("If statements!");
            bool isCool, isAwesome = true;
            if (isCool || isAwesome)
            {
                Console.WriteLine("You are cool or awesome!");
            }
            else if (!isCool && !isAwesome)
            {
                Console.WriteLine("You are not cool nor awesome. :(");
            }
            Console.WriteLine(getMax(5, 10)); // Comparison operators used.

            Console.WriteLine("Better calculator!");
            Console.WriteLine("Enter the first number: ");
            double num1 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter in an operator: ");
            string op = Console.ReadLine();
            Console.WriteLine("Enter the second number: ");
            double num2 = Convert.ToDouble(Console.ReadLine());
            if (op == "+")
            {
                Console.WriteLine(num1 + num2);
            }
            else if (op == "-")
            {
                Console.WriteLine(num1 - num2);
            }
            else if (op == "*")
            {
                Console.WriteLine(num1 * num2);
            }
            else if (op == "/")
            {
                Console.WriteLine(num1 / num2);
            }
            else
            {
                Console.WriteLine("ERROR! Not a valid operator!");
            }

            Console.WriteLine("Switch statements!");
            Console.WriteLine(getDay(0));

            Console.WriteLine("While loops!");
            int index = 6;
            while (index < 5)
            {
                Console.WriteLine("The index for while is " + index + ".");
                index++;
            }
            index = 6;
            do
            {
                Console.WriteLine("The index for dowhile is " + index + ".");
                index++;
            } while (index <= 5);

            Console.WriteLine("Guessing game!");
            string secretWord = "yeet";
            string guess = "";
            int guessCount = 0;
            int guessLimit = 3;
            bool outOfGuesses = false;
            while (guess != secretWord && !outOfGuesses)
            {
                if (guessCount < guessLimit)
                {
                    Console.WriteLine("Enter a guess!");
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

            Console.WriteLine("For loops!");
            for (int forIndex = 1; forIndex <= 5; forIndex++)
            {
                Console.WriteLine("The for loop index is: " + forIndex);
            }
            for (int forIndex = 0; forIndex < luckyNumbers.Length; forIndex++)
            {
                Console.WriteLine("luckyNumbers[" + forIndex + "]: " + luckyNumbers[forIndex]);
            }

            Console.WriteLine("Exponent method!");
            Console.WriteLine(GetPow(2, 3));

            Console.WriteLine("Comments!"); // This is a comment lol.

            Console.WriteLine("Exceptions!");

            Console.ReadLine();
        }

        static string Reverse(string phrase)
        {
            char[] charArray = phrase.ToCharArray(); // Load string to character array.
            Array.Reverse(charArray); // Reverse the array.
            return new string(charArray); // Return the string.
        }

        static void SayHi(string name)
        {
            Console.WriteLine("Hi " + name + "!");
        }

        static int Cubed(int num)
        {
            int cubed = num * num * num;
            return cubed;
        }

        static int GetMax(int num1, int num2)
        {
            int result;
            if (num1 > num2)
            {
                result = num1;
            }
            else
            {
                result = num2;
            }
            return result;
        }

        static string GetDay(int dayNum)
        {
            string dayName;

            switch (dayNum)
            {
                case 0:
                    dayName = "Sunday";
                    break;
                case 1:
                    dayName = "Monday";
                    break;
                case 2:
                    dayName = "Tuesday";
                    break;
                case 3:
                    dayName = "Wednesday";
                    break;
                case 4:
                    dayName = "Thursday";
                    break;
                case 5:
                    dayName = "Friday";
                    break;
                case 6:
                    dayName = "Saturday";
                    break;
                default:
                    dayName = "Invalid dayNum!";
                    break;
            }

            return dayName;
        }
        static int GetPow(int baseNum, int powNum)
        {
            int result = 1;

            for (int i = 0; i < powNum; i++)
            {
                result *= baseNum;
            }

            return result;
        }
    }
}
