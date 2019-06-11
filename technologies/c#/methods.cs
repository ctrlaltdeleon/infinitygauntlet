using System;

class Driver
{
    static void Main(string[] args)
    {
        SayHi("AC");
        SayHi("Sora");
        SayHi("Mega Man");
        Console.WriteLine(Cubed(3));

        Console.ReadLine();
    }

    static void SayHi(string phrase)
    {
        Console.WriteLine($"Hi {phrase}!");
    }

    static int Cubed(int number)
    {
        int cubed = number * number * number;
        return cubed;
    }
}