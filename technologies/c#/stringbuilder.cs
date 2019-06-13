using System;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        StringBuilder solution = new StringBuilder();
        for (int i = 0; i < 1000; i++)
        {
            Console.WriteLine(solution.Append(i).Append(" "));
        }

        Console.ReadLine();
    }
}