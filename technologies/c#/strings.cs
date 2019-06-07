using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Strings!");
        string phrase = "nice one";
        Console.WriteLine(phrase[0]); // "n".
        Console.WriteLine(phrase.IndexOf("one")); // Finds the first occurrence, which is at 5.

        Console.ReadLine();
    }
}

