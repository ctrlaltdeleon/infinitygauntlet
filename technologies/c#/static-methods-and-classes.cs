using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Giraffe
{
    // Creates production on the class level rather than the object level.
    static class UsefulTools
    {
        // No object required, just the parameter.
        public static void sayHi(string name)
        {
            Console.WriteLine("Hi " + name);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            // We could do `UsefulTools tool1 = new UsefulTools();` if the class was not static.
            UsefulTools.sayHi("AC");

            Console.ReadLine();
        }
    }
}
