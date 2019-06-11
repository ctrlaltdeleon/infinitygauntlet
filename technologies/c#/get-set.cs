using System;

class Movie
{
    public string title;
    public string director;
    // Only code that is in the class can access the private.
    private string rating;

    public Movie(string aTitle, string aDirector, string aRating)
    {
        title = aTitle;
        director = aDirector;
        // References the method `Rating`.
        Rating = aRating;
    }

    public string Rating
    {
        get { return rating; }
        // Users must use one of these, keeps the program secure.
        set
        {
            if (value == "G" || value == "PG" || value == "PG-13" || value == "R" || value == "NR")
            {
                rating = value;
            }
            else
            {
                rating = "NR";
            }
        }
    }
}
class Driver
{
    static void Main(string[] args)
    {
        // G, PG, PG-13, R, NR
        Movie movie1 = new Movie("The Avengers", "Joss Whedon", "Dog");
        Movie movie2 = new Movie("Shrek", "Adam Adamson", "PG");

        Console.WriteLine(movie1.Rating);
        Console.WriteLine(movie2.Rating);
        Console.ReadLine();
    }
}
