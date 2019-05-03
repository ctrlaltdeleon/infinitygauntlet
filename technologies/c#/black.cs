using System;

public class Person
{
    private string name; // The "name" field.
    public string Name // The "Name" property.
    {
        get
        {
            return name;
        }
        set
        {
            Name = value ?? String.Empty;
        }
    }
}

class TestPerson
{
    static void Main()
    {
        Person p = new Person();
        p.Name = "this is a name";  // The set accessor is invoked here.
        Console.WriteLine(p.Name); // Invokes the get accessor.
        Console.ReadKey(); // Holds the output until a key is pressed.
    }
}