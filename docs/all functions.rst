All Functions
=============
**This is the documentation for v0.3.1.** Please check if you have the correct compiler version of eng.

Output
------
say *text*
************
Prints text onto the console.

Arguments
^^^^^^^^^
* **Text** *text* - the text that will be printed. 

Examples
^^^^^^^^
::

   say "hello world"

returns:
::

   hello world

Variables & Data
----------------
let '*name*' be *value* / set '*name*' to *value*
*************************************************
Declares a variable.

Arguments
^^^^^^^^^
* **Text** *name* - the name of the new variable.
* **Any** *value* - the value assigned to the variable.

Examples
^^^^^^^^
::

   set 'x' to 334
   let 'name' be "John"

add *number* to '*name*'
************************
Adds a number to a variable.

Arguments
^^^^^^^^^
* **Whole number/Decimal** *number* - the amount to be added to the variable.
* **Text** *name* - the name of the variable that you will add to.

Examples
^^^^^^^^
::

   add 5 to 'donuts'

subtract *number* from '*name*'
*******************************
Subtracts a number from a variable.

Arguments
^^^^^^^^^
* **Whole Number/Decimal** *number* - the amount to be subtract from the variable.
* **Text** *name* - the name of the variable that you will subtract from.

Examples
^^^^^^^^
::

   subtract 1 from 'timer'

Loops
----------------
repeat *iterations* times:
*************************************************
Repeats a block of code several times.

Arguments
^^^^^^^^^
* **Whole Number > 0** *iterations* - the number of iterations of the block of text.

Examples
^^^^^^^^
::

   let 'x' be 0
   repeat 5 times:
   - add 1 to 'x'
   - say "The number is now <x>"

repeat forever:
***************
Repeats a block of code forever until the program is stopped.

Examples
^^^^^^^^^
::

   let 'x' be 0
   repeat forever:
   - add 1 to 'x'
   - say "The number is now <x>"

Time
----
wait for *s* second(s) / wait for *ms* millisecond(s)
*****************************************************
Wait for an amount of time. Note that the 's' at the end is optional.

Arguments
^^^^^^^^^
* **Whole Number/Decimal** *s*/*ms* - the number of seconds or milliseconds to wait.

Examples
^^^^^^^^
::

   wait for 1 second
   wait for 300 milliseconds

Miscellaneous
-------------
note: *comment*
***************
One-line comment. This will make the compiler skip the line. Cannot be placed at end of another function.

Examples
^^^^^^^^
::

   note: adds 3 to variable x

jump to *ID*
************
Jumps to a marker.

Arguments
^^^^^^^^^
* **Marker ID** *ID** - the ID of the marker you want to jump to. Note that markers ignore loops.

Examples
^^^^^^^^
::

   jump to after increasing x
   add 1 to 'x'
   * after increasing x

throw error *code*
******************
Manually throw an error.

Arguments
^^^^^^^^^
* **Error code** *code* - code of the error thrown.

Examples
^^^^^^^^
::

   throw error 1.1

returns:
::

   eng error 1.1 on Line 1: No variable name specified
