using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Giraffe
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 100; i++)
            {
                string phrase = "";
                if (i % 3 == 0)
                {
                    phrase += "Fizz";
                }
                if (i % 5 == 0)
                {
                    phrase += "Buzz";
                }
                Console.WriteLine(i + ":" + phrase);
            }

            Console.ReadLine();
        }
    }
}
