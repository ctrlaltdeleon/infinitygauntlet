using System;

using First;
using Second;

namespace First
{
    public class Hello
    {
        public void sayHello()
        {
            Console.WriteLine("Hello Namespace");
        }
    }
}

namespace Second
{
    public class Welcome
    {
        public void sayWelcome()
        {
            Console.WriteLine("Welcome Namespace");
        }
    }
}
public class TestNamespace
{
    public static void Main()
    {
        // If not using `using`, would reference in this way.
        // First.Hello h1 = new First.Hello();  
        // Second.Hello h2 = new Second.Hello();  
        Hello h1 = new Hello();
        Welcome w1 = new Welcome();
        h1.sayHello();
        w1.sayWelcome();

        Console.ReadLine();
    }
}