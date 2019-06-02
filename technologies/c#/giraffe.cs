using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// 2:02:00

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

            Console.WriteLine("Addition Calculator!");
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
            Cubed(3);

            Console.WriteLine("If statements!");
            bool isCool, isAwesome = true;
            if (isCool)
            {
                Console.WriteLine("You are cool!");
            }
            else if (isAwesome)
            {
                Console.WriteLine("You are awesome!");
            }
            else if (!isCool && !isAwesome)
            {
                Console.WriteLine("You are not cool nor awesome. :(");
            }

            Console.ReadLine();
        }

        public static string Reverse(string phrase)
        {
            char[] charArray = phrase.ToCharArray(); // Load string to character array.
            Array.Reverse(charArray); // Reverse the array.
            return new string(charArray); // Return the string.
        }

        static void SayHi(string name)
        {
            Console.WriteLine("Hi " + name + "!");
        }

        static int Cubed(int number)
        {
            int cubed = number * number * number;
            return cubed;
        }
    }
}
