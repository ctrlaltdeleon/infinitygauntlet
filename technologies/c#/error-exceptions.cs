using System;

class Driver
{
    static void Main(string[] args)
    {
        try
        {
            Console.Write("Enter a number: ");
            int num1 = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter another number: ");
            int num2 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(num1 / num2);
        }
        catch (Exception e) // Could replace DivideByZeroException if wanting that specific exception.
        {
            Console.WriteLine("Error: " + e.Message);
        }
        // `catch(FormatException e)` for input string format.
        finally
        {
            Console.WriteLine("Finally always executes after the try and catch blocks.");
        }

        Console.ReadLine();
    }
}

