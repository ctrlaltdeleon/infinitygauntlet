using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Program
{
    class Chef
    {
        public int recipeNumber;
        public string recipeName;

        public void MakeChicken()
        {
            Console.WriteLine("Chicken made!");
        }

        public void MakeSalad()
        {
            Console.WriteLine("Salad made!");
        }

        // Examples of overloading, taking different parameters for the same function.
        public void SearchRecipe(int recipeNumber)
        {
            Console.WriteLine("Looking for recipe #" + recipeNumber);
        }

        public void SearchRecipe(string recipeName)
        {
            Console.WriteLine("Looking for recipe " + recipeName);
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
            chef.SearchRecipe(1);
            chef.SearchRecipe("ramen");

            ItalianChef italianChef = new ItalianChef();
            italianChef.MakeChicken();
            italianChef.MakeSpecial();

            Console.ReadLine();
        }
    }
}
