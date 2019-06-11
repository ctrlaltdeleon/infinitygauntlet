using System;

class Driver
{
    static void Main(string[] args)
    {
        string phrase = "nice one";
        Console.WriteLine(phrase[0]); // "n".
        Console.WriteLine(phrase.IndexOf("one")); // Finds the first occurrence, which is at 5.

        Console.ReadLine();
    }
}

