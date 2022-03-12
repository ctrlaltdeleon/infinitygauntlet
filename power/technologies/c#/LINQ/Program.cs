using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

namespace LINQ
{
    // Language Integrated Query (LINQ) provides
    // many tools for working with data.
    // LINQ is similar to SQL, but it can work
    // with data aside from databases.
    // You manipulate data using Query Expressions.

    class Program
    {

        static void Main(string[] args)
        {
            QueryStringArray();

            QueryIntArray();

            QueryArrayList();

            QueryCollection();

            QueryAnimalData();

            Console.ReadLine();
        }

        static void QueryStringArray()
        {
            string[] dogs = { "K 9", "Brian Griffin", "Scooby Doo", "Old Yeller", "Rin Tin Tin", "Benji", "Charlie B. Barkin", "Lassie", "Snoopy" };

            var dogSpaces = from dog in dogs // Every entry within `dogs`.
                            where dog.Contains(" ") // Obtain the ones with spaces within.
                            orderby dog descending // Put in reverse alphabetical order.
                            select dog; // Choose those dogs.

            foreach (var i in dogSpaces)
            {
                Console.WriteLine(i);
            }
            Console.WriteLine();
        }

        static List<int> QueryIntArray()
        {
            int[] nums = { 5, 10, 15, 20, 25, 30, 35 };

            var gt20 = from num in nums
                       where num > 20
                       orderby num
                       select num;

            foreach (var i in gt20)
            {
                Console.WriteLine(i);
            }
            Console.WriteLine();

            nums[0] = 40;

            foreach (var i in gt20)
            {
                Console.WriteLine(i);
            }
            Console.WriteLine();

            Console.WriteLine($"Get Type : {gt20.GetType()}");

            var listGT20 = gt20.ToList<int>(); // Less memory, flexible, random placements.
            var arrayGT20 = gt20.ToArray(); // More memory, not flexible, for indexing.

            return listGT20;

            /* static int[] QueryIntArray()
             * 
             * return arrayGT20
             */
        }


        static void QueryArrayList()
        {
            ArrayList famAnimals = new ArrayList()
            {
                new Animal { Name = "Heidi", Height = .8, Weight = 18 },
                new Animal { Name = "Shrek", Height = 4, Weight = 130 },
                new Animal { Name = "Congo", Height = 3, Weight = 70 }
            };

            // Convert `ArrayList` into an `IEnumerable`.
            var famAnimalEnum = famAnimals.OfType<Animal>();

            var smallAnimals = from animal in famAnimalEnum
                               where animal.Weight <= 90
                               orderby animal.Name
                               select animal;

            foreach (var animal in smallAnimals)
            {
                Console.WriteLine($"{animal.Name} weighs {animal.Weight}.");
            }
            Console.WriteLine();
        }

        static void QueryCollection()
        {
            var animalList = new List<Animal>()
            {
                new Animal { Name = "German Shepherd", Height = 25, Weight = 77 },
                new Animal { Name = "Chihuahua", Height = 7, Weight = 4.4 },
                new Animal { Name = "Saint Bernard", Height = 30, Weight = 200 }
            };

            var bigDogs = from dog in animalList
                          where dog.Weight > 70 && dog.Height > 25
                          orderby dog.Name
                          select dog;

            foreach (var dog in bigDogs)
            {
                Console.WriteLine($"A {dog.Name} weighs {dog.Weight} lbs.");
            }
            Console.WriteLine();
        }

        static void QueryAnimalData()
        {
            Animal[] animals = new[]
            {
                new Animal{Name = "German Shepherd",
                Height = 25,
                Weight = 77,
                AnimalID = 1},
                new Animal{Name = "Chihuahua",
                Height = 7,
                Weight = 4.4,
                AnimalID = 2},
                new Animal{Name = "Saint Bernard",
                Height = 30,
                Weight = 200,
                AnimalID = 3},
                new Animal{Name = "Pug",
                Height = 12,
                Weight = 16,
                AnimalID = 1},
                new Animal{Name = "Beagle",
                Height = 15,
                Weight = 23,
                AnimalID = 2}
            };

            Owner[] owners = new[]
            {
                new Owner{Name = "Doug Parks",
                OwnerID = 1},
                new Owner{Name = "Sally Smith",
                OwnerID = 2},
                new Owner{Name = "Paul Brooks",
                OwnerID = 3}
            };

            var nameHeight = from a in animals
                                 // Create a new selection of a specific category.
                             select new
                             {
                                 a.Name,
                                 a.Height
                             };

            Array arrNameHeight = nameHeight.ToArray();

            foreach (var i in arrNameHeight)
            {
                Console.WriteLine(i.ToString());
            }
            Console.WriteLine();

            var innerJoin = from animal in animals
                            join owner in owners on animal.AnimalID
                            equals owner.OwnerID
                            select new { OwnerName = owner.Name, AnimalName = animal.Name };

            foreach (var i in innerJoin)
            {
                Console.WriteLine($"{i.OwnerName} owns {i.AnimalName}!");
            }
            Console.WriteLine();

            // Very complicated query!
            var groupJoin = from owner in owners // Get the `owners`.
                            orderby owner.OwnerID // Organize by `owner.OwnerID` (1, 2, 3).
                            join animal in animals // Get the `animals`.
                            on owner.OwnerID // Combine with `owner.OwnerID`.
                            equals animal.AnimalID // In which `owner.OwnerID` === `animal.AnimalID`.
                            into ownerGroup // Into a new data structure, `ownerGroup`.
                            select new
                            {
                                Owner = owner.Name,
                                Animals = from owner2 in ownerGroup
                                          orderby owner2.Name
                                          select owner2
                            };

            int totalAnimals;

            foreach (var ownerGroup in groupJoin)
            {
                Console.WriteLine(ownerGroup.Owner);
                foreach (var animal in ownerGroup.Animals)
                {
                    Console.WriteLine($"* {animal.Name}");
                }
            }
            /* Output:
             * 
             * Doug Parks
             * * German Shepherd
             * * Pug
             * Sally Smith
             * * Beagle
             * * Chihuahua
             * Paul Brooks
             * * Saint Bernard
             */
        }
    }
}