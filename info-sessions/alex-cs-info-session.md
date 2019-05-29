# ALEX CS INFO SESSION

```
Name:       27 C# Interview Questions and Answers to Know in 2019
Time:       Wednesday, November 14, 2018
Bio:        https://tinyurl.com/csharpinterview
Contact:    Alex (@aershov24), Full Stack Developer
```

Notes:

- Strictly C#.

1. What is an object?
   1. It's an instance of a class.
   2. If a class was the blueprint of the house, a physical house to work with would be the object.
2. What is managed and unmanaged code?
   1. Managed code deals with the `.NET` framework.
   2. Unmanaged code deals with no framework.
   3. The `.NET` framework is a framework designed by Microsoft which has a Common Runtime Language (CLR) and a Framework Class Library (FCL).
      1. CLR contributes to providing services such as type-safety, thread management, etc.
      2. FCL contributes to providing libraries such as `Math`, etc.
3. What is boxing and unboxing?
   1. Boxing is the process of converting a value type to the type `object` or to any interface type implemented by this value type.

```cs
// Boxing.
int i = 123;
object o = i;

// Unboxing.
o = 123;
i = (int)o;
```

4. What are generics?
   1. Allows for classes and methods to use any data type.
   2. Delays specification until called, but let's the program know it will require something.

```cs
using System;

public class GFG {

    // Generic.
    public void Display<TypeOfValue>(string msg, TypeOfValue value)
    {
        Console.WriteLine("{0}:{1}", msg, value);
    }
}

// Example class.
public class Example {

    // Main Method.
    public static int Main()
    {

        // Creating object of class GFG.
        GFG p = new GFG();

        p.Display<int>("Integer", 122);
        p.Display<char>("Character", 'H');
        p.Display<double>("Decimal", 255.67);

        return 0;
    }
}
```

5. Why can't you specify the accessibility modifier (public, private, protected) for methods inside the interface?
   1. All the methods are there to be overridden in the derived class for further specification.
6. What are reference types?
   1. Contain a reference to variables via memory location.
7. What is the difference between Interface and Abstract Class?
   1. Interface provides a template of functions, but not implemented., provides multiple inheritance
   2. Abstract class may provide state (data members) and/or implementation (methods).

```txt
All students have to follow certain UA, and all A-class students are students. Anyone can be a hero.

So, to summarize:

Student: abstract class
A-class student: concrete class
Hero: interface
```

8. What is the difference between overloading and overriding?
   1. Overloading is when a function may take different parameters when called.
      1. Think when you search someone, you can search by name, id, phone number, etc.
   2. Overriding is when a function inherited from a parent class is functioned differently.
      1. Think when you see a home page it says `Hello you!`, but when logged in it says `Hello your name!`.
9. What is the difference between Virtual method and Abstract method?
   1. Virtual method has implementation.
   2. Abstract method has no implementation.
10. What is the difference between dynamic type variables and object type variables?
    1. Dynamic type variables takes place at run time. (Skips boxing/unboxing, unsafe fast).
    2. Object type variables takes place at compile time. (Strong-typed, safe alright).
11. What is the output?

```cs
delegate void Printer();

static void Main()
{
    List<Printer> printers = new List<Printer>();

    int i=0;

    for(; i < 10; i++)
    {
        printers.Add(delegate { Console.WriteLine(i); });
    }

    foreach (var printer in printers)
    {
        printer();
    }
}

// This will print 10 ten times.
```

12. What is Expression Trees and how they used in LINQ?
    1. An Expression Tree is a data structure that contains Expressions which runs over data.
    2. In LINQ, expression trees are used to represent structured queries that target sources of data that implement `IQueryable<T>`.
       1. LINQ is being able to filter, order, and group data sources with a minimum of code using the methods attached.
13. What is marshalling and why do we need it?
    1. Marshalling is having code being able to be understood by other code.
    2. We need this because different languages and environments utilize specific conventions differently and they need to be able to understand each other.
14. What are the different ways a method can be overloaded?
    1. Changing the parameter requirement by data type, order of parameters, or number of parameters.
15. Can we have only `try` block without `catch` block?
    1. Yes, but we would need a `finally` block.
16. What are the uses of delegates?
    1. Delay execution of a method.
    2. Callback mechanism.
    3. Allows for multiple functions to be called at once.
17. Can multiple inheritance implemented?
    1. Yes through interfaces.
    2. Avoided in C# due to increasing complexity of source code.
18. What is the `yield` keyword used for in C#?
    1. Does stateful iteration.
    2. Provides a return on first encounter.
19. Name some advantages of LINQ over Stored Procedures?
    1. Type safety.
    2. Abstraction.
    3. Debugging support.
    4. Vendor agnostic.
    5. Deployment.
    6. Easier.
20. What is deep or shallow copy concept?
    1. Deep copy copes references and the object to which is referred.
    2. Shallow copy copies references only.
21. What is multicast delegate?
