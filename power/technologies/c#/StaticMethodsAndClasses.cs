using System;

// Creates production on the class level rather than the object level.
static class UsefulTools
{
    // No object required, just the parameter.
    public static void sayHi(string name)
    {
        Console.WriteLine("Hi " + name);
    }
}
class Driver
{
    static void Main(string[] args)
    {
        // We could do `UsefulTools tool1 = new UsefulTools();` if the class was not static.
        UsefulTools.sayHi("AC");

        Console.ReadLine();
    }
}

