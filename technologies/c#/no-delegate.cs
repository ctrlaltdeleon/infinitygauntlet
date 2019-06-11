using System;

public class Test
{
    public const int MAX_VALUE = 255;
    public const int MIN_VALUE = 10;

    public static void checkInt(int a)
    {
        Console.Write("checkInt result of {0}: ", a);
        if (a < MAX_VALUE && a > MIN_VALUE)
            Console.WriteLine("max and min value is valid");
        else
            Console.WriteLine("max and min value is not valid");
    }

    public static void checkMax(int a)
    {
        Console.Write("checkMax result of {0}: ", a);
        if (a < MAX_VALUE)
            Console.WriteLine("max value is valid");
        else
            Console.WriteLine("max value is not valid");
    }

    public static void checkMin(int a)
    {
        Console.Write("checkMin result of {0}: ", a);
        if (a > MIN_VALUE)
            Console.WriteLine("min value is valid");
        else
            Console.WriteLine("min value is not valid");
        Console.WriteLine("");
    }
}

public class Driver
{
    public static void Main(string[] args)
    {
        Test.checkInt(1);
        Test.checkMax(1);
        Test.checkMin(1);

        Test.checkInt(10);
        Test.checkMax(10);
        Test.checkMin(10);

        Test.checkInt(20);
        Test.checkMax(20);
        Test.checkMin(20);

        Test.checkInt(30);
        Test.checkMax(30);
        Test.checkMin(30);

        Test.checkInt(254);
        Test.checkMax(254);
        Test.checkMin(254);

        Test.checkInt(255);
        Test.checkMax(255);
        Test.checkMin(255);

        Test.checkInt(256);
        Test.checkMax(256);
        Test.checkMin(256);
    }
}