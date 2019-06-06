using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Program
{
    class Chef
    {
        public void MakeChicken()
        {
            Console.WriteLine("Chicken made!");
        }

        public void MakeSalad()
        {
            Console.WriteLine("Salad made!");
        }

        // Virtual allows overriding.
        public virtual void MakeSpecial()
        {
            Console.WriteLine("Soba made!");
        }
    }

    // ItalianChef inherits the class Chef.
    class ItalianChef : Chef
    {
        public void MakePasta()
        {
            Console.WriteLine("Pasta made!");
        }

        // Method from superclass is now overridden.
        public override void MakeSpecial()
        {
            Console.WriteLine("Breadsticks made!");
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Chef chef = new Chef();
            chef.MakeChicken();
            chef.MakeSpecial();

            ItalianChef italianChef = new ItalianChef();
            italianChef.MakeChicken();
            italianChef.MakeSpecial();

            Console.ReadLine();
        }
    }
}
