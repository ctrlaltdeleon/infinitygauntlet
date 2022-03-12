using System;

class Driver
{
    static void Main(string[] args)
    {
        Console.WriteLine(GetPow(2, 3));

        Console.ReadLine();
    }
    static int GetPow(int baseNum, int powNum)
    {
        int result = 1;

        for (int i = 0; i < powNum; i++)
        {
            result *= baseNum;
        }

        return result;
    }
}