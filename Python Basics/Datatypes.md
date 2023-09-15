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

But you cannot concatenate a string literal with anything else. You can also use parentheses to break up a long string while writing a program

		str = ("This is beyond crazy because there is nothing like"
				"a beach towel that is still wet after a month in the dirty bin.")
		
		=
		
		"This is beyond crazy because there is nothing like a beach towel that is still wet after a month in the dirty bin."


### Slicing 

Slicing is a way to obtain substrings and can be used to target a specific part of a string. A value like [2:8] means from the 2nd position in a string to the 8th position. The last position will not be included in the value extracted so if you wanted true position 2 to 8 you'd have to write the range of [2:9]. Slicing also has some defaults that make writing faster. 

[:1] would indicate that the default slicing position would start at 0 (the first number of the datatype).
[4:] would indicate from position 4 to the end of the datatype
[-2:] would indicate 2 positions from the right (2nd to last) of the datatype to the end

Indexing using negative numbers means the position starts from the right of the datatype, basically being a reverse indicator of the position you're referencing.






