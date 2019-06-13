using System;
using System.Linq;

class Driver
{
    static void Main(string[] args)
    {
        // Func<Input, Return> function_name = Input => whatever you need to do to it.
        Func<int, int> square = x => x * x;
        Console.WriteLine(square(5));
        // Output:
        // 25

        Func<int, int> subtractTwo = x => x - 2;
        Console.WriteLine(subtractTwo(5));
        // Output:
        // 3

        int[] numbers = { 2, 3, 4, 5 };
        var squaredNumbers = numbers.Select(x => x * x);
        Console.WriteLine(string.Join(" ", squaredNumbers));
        // Output:
        // 4 9 16 25

        Console.ReadLine();
    }
}

