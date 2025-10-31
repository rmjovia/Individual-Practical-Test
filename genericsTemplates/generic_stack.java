// Implements a generic Stack class and demonstrates it
// with integers and strings.


import java.util.*;  // For using ArrayList internally

// Generic Stack class
// <T> means the Stack can store any data type (Integer, String, etc.)
class Stack<T> {
    private List<T> elements; // Internal list to hold stack items

    // Constructor
    public Stack() {
        elements = new ArrayList<>();
    }

    // Push operation - adds an element to the top of the stack
    public void push(T item) {
        elements.add(item);
    }

    // Pop operation - removes and returns the top element
    public T pop() {
        if (elements.isEmpty()) {
            System.out.println("Stack Underflow! Cannot pop from empty stack.");
            return null;  // Return null if stack is empty
        }
        return elements.remove(elements.size() - 1);
    }

    // Top operation - returns (but does not remove) the top element
    public T top() {
        if (elements.isEmpty()) {
            System.out.println("Stack is empty!");
            return null;
        }
        return elements.get(elements.size() - 1);
    }

    // Method to check if stack is empty
    public boolean isEmpty() {
        return elements.isEmpty();
    }
}


// Main class to test the generic Stack
public class StackDemo {
    public static void main(String[] args) {


        // Example 1: Integer Stack
        
        Stack<Integer> intStack = new Stack<>();
        intStack.push(10);
        intStack.push(20);
        intStack.push(30);

        System.out.println("Top element (int): " + intStack.top());
        System.out.println("Popped: " + intStack.pop());
        System.out.println("Top after pop: " + intStack.top());

        // Example 2: String Stack
        
        Stack<String> stringStack = new Stack<>();
        stringStack.push("Hello");
        stringStack.push("World");

        System.out.println("\nTop element (string): " + stringStack.top());
        System.out.println("Popped: " + stringStack.pop());
        System.out.println("Top after pop: " + stringStack.top());
    }
}
