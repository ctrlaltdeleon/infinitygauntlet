using System;

class Driver
{
    static void Main(string[] args)
    {
        WhileLoopExample();

        Console.ReadLine();
    }

    static void WhileLoopExample()
    {
        int index = 1;
        while (index <= 5)
        {
            Console.WriteLine("The index for while is " + index + ".");
            index++;
        }

        // Performs at least once if doing `do while`.
        index = 1;
        do
        {
            Console.WriteLine("The index for dowhile is " + index + ".");
            index++;
        } while (index <= 5);
    }
}