using System;

class Driver
{
    static void Main(string[] args)
    {
        Console.Write("Enter the first number: ");
        double num1 = Convert.ToDouble(Console.ReadLine());
        Console.Write("Enter in an operator: ");
        string op = Console.ReadLine();
        Console.Write("Enter the second number: ");
        double num2 = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine($"Solution: {Calculator(op, num1, num2)}");

        Console.ReadLine();
    }

    static double Calculator(string op, double num1, double num2)
    {
        if (op == "+")
        {
            return Addition(num1, num2);
        }
        else if (op == "-")
        {
            return Subtraction(num1, num2);
        }
        else if (op == "*")
        {
            return Multiplication(num1, num2);
        }
        else if (op == "/")
        {
            return Division(num1, num2);
        }
        else
        {
            throw new Exception("ERROR! Not a valid operator!");
        }
    }

    static double Addition(double num1, double num2)
    {
        return num1 + num2;
    }

    static double Subtraction(double num1, double num2)
    {
        return num1 - num2;
    }

    static double Multiplication(double num1, double num2)
    {
        return num1 * num2;
    }

    static double Division(double num1, double num2)
    {
        return num1 / num2;
    }
}