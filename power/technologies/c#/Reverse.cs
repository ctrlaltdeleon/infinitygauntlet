using System;

class Driver
{
    static void Main(string[] args)
    {
        string phrase = "this string reversed";

        Console.WriteLine(phrase);
        Console.WriteLine(Reverse(phrase));

        Console.WriteLine(phrase);
        Console.WriteLine(ReverseLoop(phrase));

        Console.ReadLine();
    }

    static string Reverse(string phrase)
    {
        char[] reversed = phrase.ToCharArray(); // Load the string ToCharArray() by making a char[] data structure.
        Array.Reverse(reversed);                // Reverse the array using Array function Reverse().
        return new string(reversed);            // Return the new string of the array.
    }

    static string ReverseLoop(string phrase)
    {
        char[] reversed = phrase.ToCharArray();
        // Reverse method, but within the for loop.
        for (int i = 0, j = phrase.Length - 1; i < j; i++, j--)
        {
            reversed[i] = phrase[j];
            reversed[j] = phrase[i];
        }
        return new string(reversed);
    }
}