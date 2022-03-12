using System;

class Driver
{
    static void Main(string[] args)
    {
        int num = 5;
        Console.WriteLine(num / 2); // Returns an integer.
        Console.WriteLine(num / 2.0); // Returns a decimal.
        Console.WriteLine(Math.Abs(-num)); // Calling methods.
        Console.WriteLine(Math.Max(num, num + 5)); // Finds the max number between 2 parameters.

        Console.ReadLine();
    }
}