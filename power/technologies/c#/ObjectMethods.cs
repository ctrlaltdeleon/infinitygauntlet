using System;

class Student
{
    public string name;
    public string major;
    public double gpa;

    public Student(string aName, string aMajor, double aGpa)
    {
        name = aName;
        major = aMajor;
        gpa = aGpa;
    }

    public bool HasHonors()
    {
        if (gpa >= 3.5)
        {
            return true;
        }
        return false;
    }
}

class Driver
{
    static void Main(string[] args)
    {
        Student student1 = new Student("AC", "Computer Science", 3.5);

        Console.WriteLine(student1.HasHonors());

        Console.ReadLine();
    }
}