using System;

class Driver
{
    static void Main(string[] args)
    {
        int[] luckyNumbers = { 4, 8, 15, 42, 69, 420 };

        ForLoopExample(luckyNumbers);

        Console.ReadLine();
    }

    static void ForLoopExample(int[] luckyNumbers)
    {
        for (int forIndex = 1; forIndex <= 5; forIndex++)
        {
            Console.WriteLine("The for loop index is: " + forIndex);
        }

        for (int forIndex = 0; forIndex < luckyNumbers.Length; forIndex++)
        {
            Console.WriteLine("luckyNumbers[" + forIndex + "]: " + luckyNumbers[forIndex]);
        }
    }
}