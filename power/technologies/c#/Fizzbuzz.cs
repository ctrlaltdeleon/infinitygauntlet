using System;

class Driver
{
    static void Main(string[] args)
    {
        for (int i = 1; i <= 100; i++)
        {
            string phrase = "";
            if (i % 3 == 0)
            {
                phrase += "Fizz";
            }
            if (i % 5 == 0)
            {
                phrase += "Buzz";
            }
            Console.WriteLine(i + ":" + phrase);
        }

        Console.ReadLine();
    }
}