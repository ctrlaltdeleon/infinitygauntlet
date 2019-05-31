using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// 1:21:20

namespace Giraffe
{
    class Program
    {
        static void Main(string[] args)
        {
            string phrase = "nice one";
            Console.WriteLine(phrase[0]); // "n".
            Console.WriteLine(phrase.IndexOf("one")); // Finds the first occurrence, which is at 5.

            int num = 5;
            Console.WriteLine(num / 2); // Returns an integer.
            Console.WriteLine(num / 2.0); // Returns a decimal.
            Console.WriteLine(Math.Abs(-num)); // Calling methods.
            Console.WriteLine(Math.Max(num, num + 5)); // Finds the max number between 2 parameters.

            Console.Write("Enter your name: ");
            string name = Console.ReadLine(); // Allocate user input to a string data type.
            Console.WriteLine("Hello " + name);

            Console.Write("Addition Calculator!");
            Console.Write("Enter a number: ");
            double num1 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter another number: ");
            double num2 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(num1 + num2);

            Console.Write("Mad lib!");
            string color, pluralNoun, celebrity;
            Console.Write("Enter a color: ");
            color = Console.ReadLine();
            Console.Write("Enter a plural noun: ");
            pluralNoun = Console.ReadLine();
            Console.Write("Enter a celebrity: ");
            celebrity = Console.ReadLine();
            Console.WriteLine("Roses are " + color);
            Console.WriteLine(pluralNoun + " are blue");
            Console.WriteLine("I love " + celebrity);

            Console.ReadLine();
        }

        public static string Reverse(string phrase)
        {
            char[] charArray = phrase.ToCharArray(); // Load string to character array.
            Array.Reverse(charArray); // Reverse the array.
            return new string(charArray); // Return the string.
        }
    }
}
