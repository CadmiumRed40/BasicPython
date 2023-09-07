## Int

Used to represent integer number values.

ex: 1 ,2 ,45, 23,465

## Float 

Used to represent numbers with decimals or fractioned numbers.

ex: 3.14, 4.20, 6.9

#### Add. Notes:

Python also supports Decimal and Fraction conversion declarations of values as well as the j or J suffix to represent the imaginary part of an equation (ex: 3 + 4j ). Also, you can use the 'underscore' value '_' to represent the previous value given in the interpreter.

ex: 
$~ tax = 12.5 / 100
$~ price = 100.50
$~ price * tax
$~ 12.5625
$~ price + _
$~ 113.0625
$~ round( _ , 2)
$~ 113.06

## Str

Also known as strings, they represent different kinds of text from letters to symbols. You can quote text by using single or double quotes (' ' or " "). To quote a quote you need to escape it using the backslash (ex. "\\"hello"\\, they said"  would read "hello", they said.). 

\\n also escapes text and brings the next part of the string following it onto a new line.

r before the first quote would express the string as a string in its raw form with no special characters.

Using triple quotes can also express string literals in multiple lines. 

ex:
	""" 
		Mr: Hello good sir how are you?
		Sir: Not well.
		Mr: I can see we are Scandanavian.
	"""

#### Concatenation

You can concatenate strings using the + operator and repeat strings a desired amount using the * operator.

print( 3 * 'string' + 'less' ) = 'stringstringstringless'

strings that sit next to each other are automatically concatenated.

print( 'py' 'thon') = 'python'

But you cannot concatenate a string literal with anything else.






