using System;

class Driver
{
    static void Main(string[] args)
    {
        bool isCool, isAwesome;
        isCool = isAwesome = true;
        if (isCool || isAwesome)
        {
            Console.WriteLine("You are cool or awesome!");
        }
        else if (!isCool && !isAwesome)
        {
            Console.WriteLine("You are not cool nor awesome. :(");
        }
        Console.WriteLine(getMax(5, 10)); // Comparison operators used.

        Console.ReadLine();
    }

    static int getMax(int num1, int num2)
    {
        if (num1 > num2)
        {
            return num1;
        }
        else if (num2 > num1)
        {
            return num2;
        }
        else
        {
            // Exceptions are important for this reason, if it can't satisfy the return requirement.
            throw new Exception("Both are equal!");
        }
    }
}