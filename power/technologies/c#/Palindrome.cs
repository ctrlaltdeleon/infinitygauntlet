using System;

class Driver
{
    static void Main(string[] args)
    {
        string phrase = "racecar";
        Console.WriteLine($"Is {phrase} a palindrome? {Palindrome(phrase)}");

        Console.ReadLine();
    }

    static bool Palindrome(string phrase)
    {
        for (int begin = 0, end = phrase.Length - 1; begin < end / 2; begin++, end--)
        {
            if (phrase[begin] != phrase[end])
            {
                return false;
            }
        }
        return true;
    }
}