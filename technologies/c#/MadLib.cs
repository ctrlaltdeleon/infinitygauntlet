using System;

class Driver
{
    static void Main(string[] args)
    {
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

        Console.ReadLine();
    }
}