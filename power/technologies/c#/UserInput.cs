using System;

class Driver
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter your name: ");
        string name = Console.ReadLine(); // Allocate user input to a string data type.
        Console.WriteLine("Hello " + name);

        Console.ReadLine();
    }
}