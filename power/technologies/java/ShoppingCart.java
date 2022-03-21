/*
 * Mozelle Caswell CISS 238 Java
 * Final project Shopping Cart 
 */

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.text.SimpleDateFormat;
import java.util.*;

public class ShoppingCart extends Application {

 // ArrayList to hold info from the BookProces.txt file, cart information and other required variables

 ArrayList < Book > bookList, cartList;

 ListView < Book > booksView, cartView;

 Label labelSubTotal, labelTax, labelTotal;

 double subTotal = 0, tax = 0, total = 0;

 public static void main(String[] args) {

  launch(args); // Launch the application.

 }

 // start method entry point of the application

 @Override

 public void start(Stage primaryStage) throws IOException {

  // Build the inventory ArrayLists

  readBookFile();

  // Convert the inventoryTtitles ArrayList to an ObservableList.

  ObservableList < Book > observableList = FXCollections.observableArrayList(bookList);

  // Build the Book ListView

  booksView = new ListView < > (observableList);

  // Orientation for booksView
  //booksView.setOrientation(Orientation.VERTICAL);

  // Build the Shopping Cart ListView

  cartView = new ListView < > ();

  // Create the output label for the cart subtotal.

  labelSubTotal = new Label("Sub Total: ");

  // Create the output label for the tax.

  labelTax = new Label("Tax: ");

  // Create the output label for the cart total.

  labelTotal = new Label("Grand Total: ");

  // Add To Cart Button

  Button addToCartButton = new Button("Add To Cart");

  cartList = new ArrayList < > ();

  addToCartButton.setOnAction(e -> {

   int index = booksView.getSelectionModel().getSelectedIndex();

   // Get the selected index.

   // Add the item to the cart.

   if (index != -1) {

    Book b = bookList.get(index);

    // Update the cart ArrayLists

    cartList.add(bookList.get(index));

    // Update the cartListView

    cartView.setItems(FXCollections.observableArrayList(cartList));

    // Update the subtotal

    subTotal += b.getPrice();

   }

  });

  // Remove From Cart Button

  Button removeFromCartButton = new Button("Remove From Cart");

  removeFromCartButton.setOnAction(e -> {

   // Get the selected index.

   int index = cartView.getSelectionModel().getSelectedIndex();

   if (index != -1) {

    // Update the subtotal

    subTotal -= cartList.get(index).getPrice();

    // Remove the selected item from the cart ArrayLists

    cartList.remove(index);

    // Update the cartListView

    cartView.setItems(FXCollections.observableArrayList(cartList));

   }

  });

  // Clear Cart Button

  Button clearCartButton = new Button("Clear Cart");

  clearCartButton.setOnAction(e -> {

   // Update the subtotal

   subTotal = 0;

   updateLabels();

   // Clear the cart ArrayLists

   cartList.clear();

   // Update the cartListView

   cartView.setItems(FXCollections.observableArrayList(cartList));

  });

  // Checkout Button

  Button checkoutButton = new Button("Checkout");

  final double TAX_RATE = 0.07;

  checkoutButton.setOnAction(e -> {

   // Calculate the tax

   tax = subTotal * TAX_RATE;

   // Calculate the total

   total = subTotal + tax;

   updateLabels();

   //setup dates

   String timeStamp = new SimpleDateFormat("MM-DD-YYYY HH:mm:ss").format(Calendar.getInstance().getTime());

   String fntimeStamp = new SimpleDateFormat("MM-DD-YYYY.HH.mm.ss").format(Calendar.getInstance().getTime());

   //create and open receipt file

   String filename = "Receipt-" + fntimeStamp + ".txt";

   try {

    //open file

    PrintWriter receiptFile = new PrintWriter("src/shoppingCart/" + filename);

    //create the receipt

    receiptFile.println("Receipt: " + timeStamp);

    receiptFile.printf("%-25s %-10s %-10s %-10s\n", "Title", "Quantity", "Price", "Total");

    //creating a set to get rid of duplicates

    Set < Book > bookSet = new LinkedHashSet < > (cartList);

    for (Book b: bookSet) {

     //finding quantity

     int quantity = findQuantity(b, cartList);

     receiptFile.printf("%-25s %-10d $%-9.2f $%-9.2f\n", b.getTitle(),

      quantity, b.getPrice(), b.getPrice() * quantity);

    }

    receiptFile.printf("%-25s %-10s %-10s $%-9.2f\n", "Total", "", "", subTotal);

    receiptFile.printf("%-25s %-10s %-10s $%-9.2f\n", "Tax", "", "", tax);

    receiptFile.printf("%-25s %-10s %-10s $%-9.2f\n", "Grand Total", "", "", total);

    //close the file

    receiptFile.close();

   } catch (FileNotFoundException e1) {

    e1.printStackTrace();

    System.out.println("file open error");

   }

  });

  VBox vbox1 = new VBox(addToCartButton);

  vbox1.setAlignment(Pos.CENTER);

  VBox vbox2 = new VBox(removeFromCartButton, clearCartButton, checkoutButton);

  vbox2.setSpacing(10);

  vbox2.setAlignment(Pos.CENTER);

  Label lbl1 = new Label("Pick a Book");

  Label lbl2 = new Label("Shopping Cart");

  // Put everything into a VBox

  VBox vbox = new VBox(10, lbl1, booksView, vbox1, lbl2, cartView, vbox2, labelSubTotal, labelTax, labelTotal);

  vbox.setPadding(new Insets(10));

  // Add the main VBox to a scene.

  Scene scene = new Scene(vbox, 600, 800);

  primaryStage.setScene(scene);

  primaryStage.show();

  // Set the scene to the stage aand display it.

 }

 private void updateLabels() {

  labelSubTotal.setText(String.format("Sub Total: $%.2f", subTotal));

  labelTax.setText(String.format("Tax: $%.2f", tax));

  labelTotal.setText(String.format("Grand Total: $%.2f", total));

 }

 //method to find quantity (count) of a Book b in an array list

 private int findQuantity(Book b, ArrayList < Book > list) {

  int count = 0;

  for (Book book: list) {

   if (book.getTitle().equalsIgnoreCase(b.getTitle())) {

    count++;

   }

  }

  return count;

 }

 private void readBookFile() throws IOException {

  bookList = new ArrayList < Book > ();

  String input; // To hold a line from the file

  // Open the file.

  File file = new File("src/shoppingCart/BookPrices.txt");

  Scanner inFile = new Scanner(file);

  // Read the file.

  while (inFile.hasNext()) {

   // Read a line.

   String line = inFile.nextLine();

   // Tokenize the line.

   String fields[] = line.split(",");

   Book b = new Book(fields[0].trim(), Double.parseDouble(fields[1].trim()));

   // Add the book info to the ArrayLists.

   bookList.add(b);

  }

  // Close the file.

  inFile.close();

 }

}