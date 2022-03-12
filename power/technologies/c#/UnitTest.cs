using System;

public class CalculatorTester
{
    public void TestAdd()
    {
        var calculator = new Calculator();

        if (calculator.Add(2, 2) == 4)
            Console.WriteLine("Success");
        else
            Console.WriteLine("Failure");
    }
}