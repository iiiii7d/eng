All Functions
==================
**This is the documentation for v0.2.** Please check if you have the correct compiler version of eng.

Basics
------
Note: *comment*
***************
One-line comment. This will make the compiler skip the line. Cannot be placed at end of another function.
Examples:
"""""""""
.. code-block::
   note: adds 3 to variable x

say *text*
************
Prints text onto the console.
Arguments:
""""""""""
* **Text** *text* - the text that will be printed. 

Examples:
"""""""""
.. code-block::
   say "hello world"
returns:
.. code-block::
   hello world

Variables & Data
----------------
let '*name*' be *value* / set '*name*' to *value*
*************************************************
Declares a variable.

Arguments:
""""""""""
* **Text** *name* - the name of the new variable.
* **Any** *value* - the value assigned to the variable.

Examples:
"""""""""
.. code-block::
   set 'x' to 334
   let 'name' be "John"

add *number* to '*name*'
************************
Adds a number to a variable.

Arguments:
""""""""""
* **Whole number/Decimal** *number* - the amount to be added to the variable.
* **Text** *name* - the name of the variable that you will add to.

Examples:
"""""""""
.. code-block::
   add 5 to 'donuts'

subtract *number* from '*name*'
************************
Subtracts a number from a variable.

Arguments:
""""""""""
* **Whole Number/Decimal** *number* - the amount to be subtract from the variable.
* **Text** *name* - the name of the variable that you will subtract from.

Examples:
"""""""""
.. code-block::
   subtract 1 from 'timer'

Loops
----------------
repeat *iterations* times:
*************************************************
Repeats a block of code several times.

Arguments:
""""""""""
* **Whole Number > 0** *iterations* - the number of iterations of the block of text.

Examples:
"""""""""
.. code-block::
   let 'x' be 0
   repeat 5 times:
   - add 1 to 'x'
   - say "The number is now <x>"

Miscellaneous
----------------
throw error *code*
*************************************************
Manually throw an error.

Arguments:
""""""""""
* **Error code** *code* - code of the error thrown.

Examples:
"""""""""
.. code-block::
   throw error 1.1
returns:
.. code-block::
   eng error 1.1 on Line 1: No variable name specified
