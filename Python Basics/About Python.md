
Python is a Dynamically typed, high-level language with built-in data structures that is suitable for rapid application development. 

## Typing:

In programming languages, variables are assigned "types" that indicate how the variables should be treated as well as their associated operations. Declared value types (such as string for text values, int for numbers, and bool for true and false) need to match up to the values that they are assigned. This also applies to the arguments and functions that call for them as well.

### Methods of handling typing:

##### Static Typing:

The variables are declared and set before compiling in a statically typed language. For example:

string a =  'abc' //text
int b = 123 //number
b = "abc" // returns an error

B would return an error because at compilation b is defined as a number and cannot accept the change as a string. This is also a more risk-averse style of handling programming because error handling happens at compilation.
##### Dynamic Typing: 

With dynamic typing, you don't have to define the type of value the variable will be assigned, and can be changed mid-execution of the program. For example:

let a = "abc" // string
let b = 10 // integer

b = "abc" // b is now a string

This method leaves out the particulars of handling variables and programmers can focus on the logic. One problem is that it can lead to lazy coding practices and have bugs more embedded and harder to find, especially as time goes on 

##### Strongly-typed vs. Weakly-typed

Dynamic and static typing can often be confused with strong and weakly typed handling of variables. In Javascript, variables are weakly typed, meaning Javascript makes assumptions about what a variable means during execution. For example false = 0 and true = 1 in its integer equivalent so typing (4+true) would equal 5 or (4-false) would equal 4 because of its assumed integer value. Python is strongly typed, meaning its variables are strict in their definition and leave little room for misinterpretation.
### Summary: 

In short, Python is a dynamic, strongly typed language. Meaning that its variables can be defined and redefined through its compilation and as the variables are defined they remain clear and are not misinterpreted as the program runs. Errors will be caught if definitions are unclear or a conflict is found between variables and functions, allowing the author to fix the error before the program crashes.

#Dynamic-Typing #Strongly-Typed