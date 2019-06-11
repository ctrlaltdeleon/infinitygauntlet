using System;

class Driver
{
    static void Main(string[] args)
    {
        string phrase = "this string reversed";

        Console.WriteLine(phrase);
        Console.WriteLine(Reverse(phrase));

        Console.ReadLine();
    }

    static string Reverse(string phrase)
    {
        char[] reversed = phrase.ToCharArray(); // Load the string ToCharArray() by making a char[] data structure.
        Array.Reverse(reversed);                // Reverse the array using Array function Reverse().
        return new string(reversed);            // Return the new string of the array.
    }
}
