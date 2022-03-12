using System;

class Book
{
    // Class attributes.
    public string title;
    public string author;
    public int pages;

    // Constructor, deconstructor, and polymorphism.
    public Book()
    {
        Console.WriteLine("Constructor called, creating book...");
    }

    ~Book()
    {
        Console.WriteLine("Deconstructor called, book destroyed...");
    }

    public Book(string aTitle, string aAuthor, int aPages)
    {
        Console.WriteLine("Creating book...");
        title = aTitle;
        author = aAuthor;
        pages = aPages;
    }
}

class Driver
{
    static void Main(string[] args)
    {
        // Instance of a class, an object.
        Book book1 = new Book();
        book1.title = "Harry Potter";
        book1.author = "JK Rowling";
        book1.pages = 400;

        Book book2 = new Book();
        book2.title = "Lord of the Rings";
        book2.author = "Tolkein";
        book2.pages = 700;

        Book book3 = new Book("The Great Gatsby", "F. Scott Fitzgerald", 218);

        Console.WriteLine(book1.title);
        Console.WriteLine(book1.author);
        Console.WriteLine(book1.pages);

        Console.WriteLine(book3.title);
        Console.WriteLine(book3.author);
        Console.WriteLine(book3.pages);

        Console.ReadLine();
    }
}
