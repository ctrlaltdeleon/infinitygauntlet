# JAVA FOR DUMMIES

## 2: All About Software

### Quick-Start Instructions

- Install the Java Development Kit (JDK):
  - Look for Standard Edition (SE).
  - If you see a number like this:
    - "9u3"
    - This means "The 3rd update of Java 9".
- Install an integrated development environment:
  - Eclipse
  - Intellij IDEA
  - NetBeans
- Test your installed software:
  - Launch IDE.
  - Create new Java project.
  - File > New > Class
  - Edit the new .java file with some "hello world".
  - Run the program and check the output!

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("hello world");
    }
}
```

### What Did I Install on My Computer?

- From the IDE you installed a compiler and java virtual machine.
- Steps on how your code gets interpreted:
  - Javs source code.
    - What the developers want to deliver.
  - Compiler.
    - Changes the code to byte code, transition from human to computer language.
  - Bytecode.
    - Packages Java source code to be disgesetable by Java virtual machines.
  - Java virtual machines.
    - Packages bytecode to be digestable by OS code.
  - OS code.
    - Opens code to be digestable by users.
  - The user!
    - That's you!
