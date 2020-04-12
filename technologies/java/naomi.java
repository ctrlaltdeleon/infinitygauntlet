import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;
import java.util.Random;

class Main {
	public static void main(String args[]) {
    // Part 1.
    // Prereq to read user input.
		Scanner in = new Scanner(System.in);
    // Prompt.
    System.out.println("Input the number of elements in the lists:");
		// Reads user input.
    int num = in.nextInt();
		// Read in N elements to init and fill an array named "list".
		Integer[] list = new Integer[num];
		// Read in N elements to init and fill a linked list named "linked".
		ArrayList<Integer> linked = new ArrayList<Integer>(num);
    // For loop to take user input into data structure.
		for (int i = 0; i < num; i++) {
        System.out.println("Input number " + (i+1) + "...");
        int temp = in.nextInt();
        list[i] = temp;
        linked.add(i,temp);
		}
    // Show outputs of the array and linked list.
    System.out.println("Printing array...");
    System.out.println(Arrays.toString(list));
    System.out.println("Printing linked list...");
    System.out.println(linked.toString());
    // User input to take in a key number to search for.
    System.out.println("Input the key number to look for:");
    Integer var = in.nextInt();
    // Run linear search function (essentianlly a boolean).
    int result = Main.linearSearch(list, var);
    // Alternate method, but no need to: keyfound ? result : notfound.
    if (result == -1 ) {
      System.out.println("Key "+ var + " was not found");
    } else { 
      System.out.println("Key " + var + " was found at position " + result);
    }
    // Run max search function.
    result = Main.max(list);
    System.out.println(result + " is the max element");
    // Part 2.
    // Reads user input.
    System.out.println("Integer m for first dimension (row) of a 2-D array:");
    int m = in.nextInt();
    System.out.println("Integer p for second dimension (column) of a 2-D array:");
    int p = in.nextInt();
    // Initialize data structure of 2-d array.
    Integer[][] list2 = new Integer[m][p];
    // Read in m x p elements to fill 'list2'.
    for (int row = 0; row < list2.length; row++) {        
      for ( int col = 0 ; col < list2[row].length; col++) {
        System.out.print("Insert a value at list2[" + row + "][" + col + "]:");
        list2[row][col] = in.nextInt();
      }
    }
    // Display 'list2'.
    for (int row = 0; row < list2.length; row++) {  
      for (int col = 0 ; col < list2[row].length; col++) {
          System.out.print(list2[row][col]+ " "); 
      }
      System.out.println(" ");  
    }
    // So the fix here was the declarations of the 2-d array and reading user input.
    // There's very strict ruling with "int" VS "Integer" and it gets confusing with Java.
    // It's because it's a primitive VS a class.
    // Instead of "int[][] list2 = new int[m][p];".
    // We do "Integer[][] list2 = new Integer[m][p];".
    result = Main.max(list2);
    // Call max(list2) and print the result.
    System.out.println(result + " is the max element");
    // Instantiate an ArrayList of type Integer named 'alist' from 'linked' (meaning 'alist' is a copy of 'linked').
    ArrayList<Integer> alist = new ArrayList<Integer>(linked);
    // Print out 'alist' using System.out.println(alist).
    System.out.println(alist);
    // Call removeDuplicates using 'alist' as the parameter.
    alist = removeDuplicates(alist);
    // Print the now unique 'alist' using ``.
    System.out.println(alist);
    // Call shuffle using 'alist' as the parameter.
    Main.shuffle(alist);
    // Print 'alist' again using ``.
    System.out.println(alist);
    // Find the max element of 'alist' and print the result.
    result = Main.max(alist);
    System.out.println(result + " is the max element");
	}
			
	public static <E> ArrayList<E> removeDuplicates(ArrayList<E> list) {
    // Create a new list called "templist" that has no duplicates in it.
    ArrayList<E> tempList = new ArrayList<>(list.size());
      // For the new list compared to the old list.
      for (E aList : list) {
        // If the new list does not contain something shown, add it to the new list.
        // So this means if the new list sees something already inside it, skip it.
        if (!tempList.contains(aList)) {
          tempList.add(aList);
          }
      }
    return tempList;
	}
	
	public static <E> void shuffle(ArrayList<E> alist) {
    // Simple solution.
		// Collections.shuffle(alist);
    // Solution for the prompt.
    // size() is number of elements while length() is capacity, slight difference.
    for (int i = 0; i < alist.size(); i++) {
      // Following prompt, using Random class.
      Random randomNumber = new Random();
      // Chooses a number from 0 to alist.size().
      int n = randomNumber.nextInt(alist.size());
      // Gets the number and is put temporarily.
      E temp = alist.get(n);
      // Sets the number into a specific spot, thus "shuffling".
      alist.set(n, alist.get(i));
      // It's a bubble sort.
      alist.set(i, temp);
    }
	}
	
	public static <E extends Comparable<E>> E max(ArrayList<E> list) {
		E maxValue = list.get(0);
		for (int i = 1; i <list.size(); i++)
		{
			 if (list.get(i).compareTo(maxValue) > 0) 
			 {
				 maxValue = list.get(i);
			 }
		}
		return maxValue;
	}
	
	public static <E extends Comparable<E>> int linearSearch(E[] list, E key) {
    for (int i = 0; i < list.length; i++)
      {
        if (list[i].compareTo(key) == 0) 
        {
          return i;
        }
      }
    return -1;
	}
	
	public static <E extends Comparable<E>> E max(E[] list) {
		E maxValue = list[0];
		for (int i = 1; i <list.length; i++)
		{
      if (list[i].compareTo(maxValue) > 0) 
      {
        maxValue = list[i];
      }
		}
		return maxValue;
	}
	
	public static <E extends Comparable<E>> E max(E[][] list) {
		E maxValue = list[0][0];
		for (int i = 1; i < list.length; i++) {
			for (int j = 1; j < list[i].length; j++) {
        if (list[i][j].compareTo(maxValue) > 0) 
        {
          maxValue = list[i][j];
        }
			}
		}
		return maxValue;
	}
	
	public String getIdentificationString() {
		return "Program 7, Naomi Ocampo";
	}
}
